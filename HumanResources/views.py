# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django Imports.
import operator

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.db.models import Q

# Model Imports.
from HumanResources.models import *
from django.template import Context


# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext,loader

def employeehome(request):
    return render(request, 'admin/HumanResources/employee-home.html')

def payrollhome(request):
    return render(request, 'admin/HumanResources/payroll-home.html')

class JobInstanceListView(generic.ListView):
    model = JobInstance
    template_name = "HumanResources/job-instance-list.html"

    def get_context_data(self, **kwargs):
        context = super(JobInstanceListView, self).get_context_data(**kwargs)

        elements = context['object_list']

        first_node = JobInstance.objects.get(pk=1)

        first_node.children = self.get_children(first_node)

        context['chart'] = self.get_chart(first_node)

        print '----'
        print context['chart']

        return context

    def get_children(self, node):
        children = JobInstance.objects.filter(parent_job_instance_id=node.id)
        for child in children:
            child.children = self.get_children(child)

        return children

    def get_chart(self, first_node):
        html = '<ul id="org" style="display:none">'

        html += '<li>'
        html += str(first_node.id)

        html += self.get_sub_chart(first_node.children)

        html += '</li>'
        html += '</ul>'

        return html

    def get_sub_chart(self, children):
        html = ''
        if children is not None and len(children) > 0:
            html += '<ul>'

        for child in children:
            html += '<li>' + str(child.id)
            html += self.get_sub_chart(child.children)
            html += '</li>'

        if children is not None and len(children) > 0:
            html += '</ul>'

        return html

class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = "HumanResources/employee-detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)

        # The employee object.
        employee = context['employee']

        # Obtaining the test applications of the employee and setting them to the context.
        test_applications = TestApplication.objects.filter(employee__id=employee.id)
        context['test_applications'] = test_applications

        # Obtaining the education info of the employee and setting it to the context.
        context['education'] = Education.objects.filter(employee__id=employee.id)

        # Obtaining the current education info of the employee and setting it to the context.
        current_education_array = []
        current_education_set = CurrentEducation.objects.filter(employee__id=employee.id)
        for record in current_education_set:
            record_json = {
                'type': record.get_type_display(),
                'name': record.name,
                'institution': record.institution,
                'sunday': record.sunday,
                'monday': record.monday,
                'tuesday': record.tuesday,
                'wednesday': record.wednesday,
                'thursday': record.thursday,
                'friday': record.friday,
                'saturday': record.saturday,
                'documents': []
            }

            # Obtaining the documents for the current education record.
            document_set = CurrentEducationDocument.objects.filter(current_education__id=record.id)
            for document in document_set:
                record_json['documents'].append(document)

            current_education_array.append(record_json)

        context['current_education'] = current_education_array

        # Obtaining the emergency contact info of the employee and setting it to the context.
        context['emergency_contacts'] = EmergencyContact.objects.filter(employee__id=employee.id)

        # Obtaining the family member info of the employee and setting it to the context.
        context['family_members'] = FamilyMember.objects.filter(employee__id=employee.id)

        # Obtaining the work references info of the employee and setting it to the context.
        context['work_references'] = WorkReference.objects.filter(employee__id=employee.id)

        # Obtaining the employee's documents and setting them to the context.
      #  context['employee_documents'] = EmployeeDocument.objects.filter(employee__id=employee.id)

        # Obtaining the employee's checker info and setting it to the context.
        #context['checker_data'] = CheckerData.objects.get(employee__id=employee.id)

        # Obtaining the employee's position description and setting it to the context.
        context['employee_position_description'] = EmployeePositionDescription.objects.filter(employee__id=employee.id)

        # Obtaining the employee's Employee Financial Data and setting it to the context.
        context['employee_financial_data'] = EmployeeFinancialData.objects.filter(employee__id=employee.id)

        return context


'''@login_required()
def EmployeeByPeriod(request):
    model = EmployeePositionDescription
    template_name = "admin/HumanResources/employee_by_payroll.html"

    context = Context({"my_name": "Dolores"})
    template = loader.get_template('admin/HumanResources/employee_by_payroll.html')
    payrollgroup = request.GET.get('payrollgroup')
    employees = EmployeePositionDescription.objects.values('employee__id').filter(payroll_group__id=payrollgroup)
    return HttpResponse(template.render(context))'''


@login_required()
def EmployeeByPeriod(request):
    payrollgroup = request.GET.get('payrollgroup')
    payrollperiod = request.GET.get('payrollperiod')
    template = loader.get_template('admin/HumanResources/employee_by_payroll.html')
    employees = EmployeePositionDescription.objects.filter(payroll_group__id=payrollgroup)
    period_data = PayrollPeriod.objects.filter(id=payrollperiod)
    #context = RequestContext.request
    context = {'employees': employees,
               'payrollperiod': payrollperiod,
               'payrolldata':period_data}
    return HttpResponse(template.render(context,request))


@login_required()
def payrollhome(request):

    template = loader.get_template('admin/HumanResources/payroll-home.html')
    period_data = PayrollPeriod.objects.all().query
    employees = EmployeePositionDescription.objects.all()
    employees.group_by = ['payroll_group_id']
    period_data
    #context = RequestContext.request
    context = {'employees': employees,
               'payrolldata':period_data}
    return HttpResponse(template.render(context,request))


class PayrollPeriodListView(generic.ListView):
    model = PayrollPeriod
    template_name = "HumanResources/payroll-period-list.html"


    def get_queryset(self):
        result = super(PayrollPeriodListView, self).get_queryset()

        payroll_group_id = self.kwargs['pk']

        result = result.filter(payroll_group_id=payroll_group_id)


        return result

    def get_context_data(self, **kwargs):
        context = super(PayrollPeriodListView, self).get_context_data(**kwargs)

        payroll_group_id = self.kwargs['pk']
        payroll_group = PayrollGroup.objects.get(pk=payroll_group_id)

        context['payrollgroup'] = payroll_group

        return context

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('ERP.view_list_empresa'):
        #     raise PermissionDenied
        return super(PayrollPeriodListView, self).dispatch(request, args, kwargs)



class PayrollPeriodDetail(generic.ListView):
    model = Employee
    template_name = "HumanResources/payroll-period-detail.html"


    def get_queryset(self):
        result = super(PayrollPeriodDetail, self).get_queryset()

        payroll_period_id = self.kwargs['pk']

        payroll_period = PayrollPeriod.objects.get(pk=payroll_period_id)

        payroll_group_id = payroll_period.payroll_group_id


        employees = EmployeePositionDescription.objects.filter(payroll_group_id=payroll_group_id).values('employee')
        employee_ids = []


        for employee in employees:
            employee_ids.append(employee['employee'])

        result = result.filter(id__in=employee_ids)


        return result

    def get_context_data(self, **kwargs):
        context = super(PayrollPeriodDetail, self).get_context_data(**kwargs)

        payroll_period_id = self.kwargs['pk']

        payroll_period = PayrollPeriod.objects.get(pk=payroll_period_id)

        payroll_group_id = payroll_period.payroll_group_id

        payroll_group = PayrollGroup.objects.get(pk=payroll_group_id)

        context['payrollgroup'] = payroll_group
        context['payrollperiod'] = payroll_period

        return context

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('ERP.view_list_empresa'):
        #     raise PermissionDenied
        return super(PayrollPeriodDetail, self).dispatch(request, args, kwargs)




class PayrollPeriodEmployeeDetail(generic.DetailView):
    model = Employee
    template_name = "HumanResources/payroll-period-employee-detail.html"


    def get_queryset(self):
        result = super(PayrollPeriodEmployeeDetail, self).get_queryset()

        employee_id = self.kwargs['pk']

        return result

    def get_context_data(self, **kwargs):
        context = super(PayrollPeriodEmployeeDetail, self).get_context_data(**kwargs)

        employee_id = self.kwargs['pk']

        return context

    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('ERP.view_list_empresa'):
        #     raise PermissionDenied
        return super(PayrollPeriodEmployeeDetail, self).dispatch(request, args, kwargs)
