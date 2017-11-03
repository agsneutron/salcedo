# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 05:24
from __future__ import unicode_literals

import HumanResources.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ERP', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checker_type', models.IntegerField(choices=[(1, 'Autom\xe1tico'), (2, 'Manual')], default=1, verbose_name='Tipo de Checador')),
                ('checks_entry', models.BooleanField(default=True, verbose_name='Checa Entrada')),
                ('checks_exit', models.BooleanField(default=True, verbose_name='Checa Salida')),
            ],
            options={
                'verbose_name': 'Tipo de Checador',
                'verbose_name_plural': 'Tipos de Checador',
            },
        ),
        migrations.CreateModel(
            name='CurrentEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Licenciatura'), (2, 'Maestr\xeda'), (3, 'Doctorado')], default=1, verbose_name='Tipo de Educaci\xf3n')),
                ('name', models.CharField(max_length=2048, verbose_name='Nombre')),
                ('institution', models.CharField(max_length=1024, verbose_name='Instituci\xf3n')),
                ('sunday', models.BooleanField(default=False, verbose_name='Domingo')),
                ('monday', models.BooleanField(default=False, verbose_name='Lunes')),
                ('tuesday', models.BooleanField(default=False, verbose_name='Martes')),
                ('wednesday', models.BooleanField(default=False, verbose_name='Mi\xe9rcoles')),
                ('thursday', models.BooleanField(default=False, verbose_name='Jueves')),
                ('friday', models.BooleanField(default=False, verbose_name='Viernes')),
                ('saturday', models.BooleanField(default=False, verbose_name='S\xe1bado')),
            ],
            options={
                'verbose_name': 'Formaci\xf3n Actual del Empleado',
                'verbose_name_plural': 'Formaciones Actuales del Empleado',
            },
        ),
        migrations.CreateModel(
            name='CurrentEducationDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=HumanResources.models.upload_employee_current_education_document, verbose_name='Archivo')),
                ('comments', models.CharField(max_length=2048, verbose_name='Comentarios')),
                ('current_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.CurrentEducation', verbose_name='Formaci\xf3n Actual del Empleado')),
            ],
            options={
                'verbose_name': 'Documento de la Formaci\xf3n Acutal del Empleado',
                'verbose_name_plural': 'Documentos de la Formaci\xf3n Acutal del Empleado',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tipo de Documento')),
            ],
            options={
                'verbose_name': 'Etiquetas',
                'verbose_name_plural': 'Tipo de Documento',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Licenciatura'), (2, 'Maestr\xeda'), (3, 'Doctorado')], default=1, verbose_name='Tipo de Educaci\xf3n')),
                ('name', models.CharField(max_length=2048, verbose_name='Nombre')),
                ('institution', models.CharField(max_length=1024, verbose_name='Instituci\xf3n')),
                ('license_code', models.CharField(max_length=512, verbose_name='C\xf3digo o N\xfamero de C\xe9dula')),
                ('evidence', models.FileField(null=True, upload_to=HumanResources.models.upload_employee_education_document, verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Formaci\xf3n Acad\xe9mica del Empleado',
                'verbose_name_plural': 'Formaciones Acad\xe9micas del Empleado',
            },
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('first_last_name', models.CharField(max_length=255, verbose_name='Apellido Paterno')),
                ('second_last_name', models.CharField(max_length=255, verbose_name='Apellido Materno')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='N\xfamero de Tel\xe9fono')),
                ('cellphone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='N\xfamero de Celular')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Correo Electr\xf3nico')),
            ],
            options={
                'verbose_name': 'Contacto de Emergencia',
                'verbose_name_plural': 'Contactos de Emergencia',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_key', models.CharField(max_length=64, verbose_name='Clave del Empleado')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('first_last_name', models.CharField(max_length=255, verbose_name='Apellido Paterno')),
                ('second_last_name', models.CharField(max_length=255, verbose_name='Apellido Materno')),
                ('type', models.IntegerField(choices=[(1, 'Empleado Tipo A'), (2, 'Empleado Tipo B')], default=1, verbose_name='Tipo de Empleando')),
                ('registry_date', models.DateField(default=datetime.datetime(2017, 11, 2, 5, 24, 44, 737153, tzinfo=utc), verbose_name='Fecha de Registro')),
                ('status', models.IntegerField(choices=[(1, 'Estatus A del Empleado'), (2, 'Estatus B del Empleado')], default=1, verbose_name='Estatus del Empleado')),
                ('birthdate', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('gender', models.IntegerField(choices=[(1, 'Femenino'), (2, 'Masculino')], default=1, verbose_name='G\xe9nero')),
                ('marital_status', models.IntegerField(choices=[(1, 'Soltero'), (2, 'Casado')], default=1, verbose_name='Estado Civil')),
                ('curp', models.CharField(max_length=18, unique=True, verbose_name='CURP')),
                ('rfc', models.CharField(max_length=13, unique=True, verbose_name='RFC')),
                ('phone_number', models.CharField(max_length=20, verbose_name='N\xfamero de Tel\xe9fono')),
                ('personal_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Correo Electr\xf3nico Personal')),
                ('work_email', models.CharField(max_length=255, verbose_name='Correo Electr\xf3nico Laboral')),
                ('social_security_number', models.CharField(max_length=20, verbose_name='N\xfamero de Seguro Social')),
                ('colony', models.CharField(max_length=255, verbose_name='Colonia')),
                ('street', models.CharField(max_length=255, verbose_name='Calle')),
                ('outdoor_number', models.CharField(max_length=10, verbose_name='No. Exterior')),
                ('indoor_number', models.CharField(max_length=10, verbose_name='No. Interior')),
                ('blood_type', models.CharField(max_length=3, verbose_name='Tipo Sangu\xedneo')),
                ('driving_license_number', models.CharField(max_length=20, verbose_name='N\xfamero de Licencia de Conducir')),
                ('driving_license_expiry_date', models.DateField(verbose_name='Fecha de Expiraci\xf3n de la Licencia de Conducir')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.Pais', verbose_name='Pa\xeds')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='ERP.Estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='EmployeeContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_key', models.CharField(max_length=128, verbose_name='Clave del Contrato')),
                ('description', models.CharField(max_length=4096, verbose_name='Descripci\xf3n del Contrato')),
                ('specifications', models.CharField(max_length=4096, verbose_name='Especificaciones del Contrato')),
                ('start_date', models.DateField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de T\xe9rmino')),
                ('base_salary', models.FloatField(verbose_name='Salario')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Contrato del Empleado',
                'verbose_name_plural': 'Contratos del Empleado',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=HumanResources.models.upload_employee_document, verbose_name='Archivo')),
                ('comments', models.CharField(max_length=2048, verbose_name='Comentarios')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.DocumentType', verbose_name='Tipo de Documento')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Documento Probatorio',
                'verbose_name_plural': 'Documentos Probatorios',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDropOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha de Baja')),
                ('type', models.IntegerField(choices=[(1, 'Despido'), (2, 'Incapacidad')], default=1, verbose_name='Tipo de Baja')),
                ('reason', models.CharField(blank=True, max_length=4096, verbose_name='Motivo')),
                ('severance_pay', models.FloatField(null=True, verbose_name='Liquidaci\xf3n')),
                ('observations', models.CharField(max_length=4096, null=True, verbose_name='Observaciones')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Baja de Empleado',
                'verbose_name_plural': 'Bajas de Empleado',
            },
        ),
        migrations.CreateModel(
            name='EmployeeHasTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Etiqueta del Empleado',
                'verbose_name_plural': 'Etiquetas del Empleado',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('first_last_name', models.CharField(max_length=255, verbose_name='Apellido Paterno')),
                ('second_last_name', models.CharField(max_length=255, verbose_name='Apellido Materno')),
                ('relationship', models.CharField(blank=True, max_length=128, verbose_name='PArentesco')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Familiar',
                'verbose_name_plural': 'Familiares',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nombre de la Etiqueta')),
            ],
            options={
                'verbose_name': 'Etiquetas',
                'verbose_name_plural': 'Etiqueta',
            },
        ),
        migrations.CreateModel(
            name='TaxRegime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='R\xe9gimen Fiscal')),
            ],
            options={
                'verbose_name': 'R\xe9gimen Fiscal',
                'verbose_name_plural': 'Reg\xedmenes Fiscales',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Nombre de la Prueba')),
            ],
            options={
                'verbose_name': 'Prueba',
                'verbose_name_plural': 'Pruebas',
            },
        ),
        migrations.CreateModel(
            name='TestApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(verbose_name='Fecha de Aplicaci\xf3n')),
                ('result', models.CharField(max_length=512, verbose_name='Resultado')),
                ('comments', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Comentarios')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Test', verbose_name='Prueba')),
            ],
        ),
        migrations.CreateModel(
            name='WorkReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la Persona que Hace la Referencia')),
                ('first_last_name', models.CharField(max_length=255, verbose_name='Apellido Paterno de la Persona que Hace la Referencia')),
                ('second_last_name', models.CharField(max_length=255, verbose_name='Apellido Materno de la Persona que Hace la Referencia')),
                ('company_name', models.CharField(max_length=255, verbose_name='Empresa')),
                ('first_phone_number', models.CharField(max_length=20, verbose_name='N\xfamero de Tel\xe9fono #1')),
                ('second_phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='N\xfamero de Tel\xe9fono #2')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Correo Electr\xf3nico')),
                ('notes', models.CharField(max_length=2048, null=True, verbose_name='Notas')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Referencia Laboral',
                'verbose_name_plural': 'Referencias Laborales',
            },
        ),
        migrations.AddField(
            model_name='employeehastag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Tag', verbose_name='Etiqueta'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tags',
            field=models.ManyToManyField(through='HumanResources.EmployeeHasTag', to='HumanResources.Tag', verbose_name='Etiquetas'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tax_regime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.TaxRegime', verbose_name='R\xe9gimen Fiscal'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tests',
            field=models.ManyToManyField(through='HumanResources.TestApplication', to='HumanResources.Test', verbose_name='Pruebas'),
        ),
        migrations.AddField(
            model_name='employee',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='estado', on_delete=django.db.models.deletion.CASCADE, to='ERP.Municipio', verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado'),
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado'),
        ),
        migrations.AddField(
            model_name='currenteducation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado'),
        ),
        migrations.AddField(
            model_name='checkerdata',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResources.Employee', verbose_name='Empleado'),
        ),
        migrations.AlterUniqueTogether(
            name='employeehastag',
            unique_together=set([('employee', 'tag')]),
        ),
    ]
