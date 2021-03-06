from django.conf.urls import url, include
from reporting import views
from DataUpload.dataUpload import *
from . import views

app_name = 'Reporting'

urlpatterns = [
    # Project Dashboard
    url(r'^get_main_dashboard', views.GetMainDashboard.as_view()),
    url(r'^get_dashboard_by_project$', views.GetDashboardByProject.as_view()),

    url(r'^get_financial_report$', views.GetFinancialReport.as_view()),
    url(r'^get_physical_financial_advance_report$', views.GetPhysicalFinancialAdvanceReport.as_view()),
    url(r'^get_estimate_report_for_contractors$', views.GetEstimateReportForContractors.as_view()),
    url(r'^get_estimate_report_by_single_contractor$', views.GetEstimateReportBySingleContractor.as_view()),
    url(r'^get_budget_by_contractor_report$', views.GetBudgetByContractorReport.as_view()),

    # Report for the estimates page.
    url(r'^get_estimates_report$', views.GetEstimatesReport.as_view()),


    url(r'^$', views.testView, name='test'),
    url(r'^', views.report, name='report'),
]
