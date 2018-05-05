# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-04 17:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SharedCatalogs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField(blank=True, null=True, verbose_name='Folio')),
                ('registry_date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Registro')),
                ('description', models.CharField(max_length=4096, verbose_name='Concepto')),
                ('reference', models.CharField(max_length=1024, verbose_name='Referencia')),
            ],
            options={
                'verbose_name': 'P\xf3liza contable',
                'verbose_name_plural': 'P\xf3lizas Contables',
            },
        ),
        migrations.CreateModel(
            name='AccountingPolicyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=4096, verbose_name='Concepto')),
                ('debit', models.FloatField(default=0, verbose_name='Debe')),
                ('credit', models.FloatField(default=0, verbose_name='Haber')),
                ('registry_date', models.DateField(verbose_name='Fecha de Registro')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Account', verbose_name='Cuenta')),
                ('accounting_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.AccountingPolicy', verbose_name='P\xf3liza')),
            ],
            options={
                'verbose_name': 'Detalle de P\xf3liza',
                'verbose_name_plural': 'Detalle de P\xf3lizas',
            },
        ),
        migrations.CreateModel(
            name='CommercialAlly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('colony', models.CharField(max_length=255, verbose_name='Colonia')),
                ('street', models.CharField(max_length=255, verbose_name='Calle')),
                ('outdoor_number', models.CharField(max_length=10, verbose_name='No. Exterior')),
                ('indoor_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='No. Interior')),
                ('zip_code', models.CharField(max_length=5, verbose_name='C\xf3digo Postal')),
                ('rfc', models.CharField(max_length=20, verbose_name='RFC')),
                ('curp', models.CharField(max_length=18, unique=True, verbose_name='CURP')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Tel\xe9fono')),
                ('phone_number_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel\xe9fono 2')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('cellphone_number', models.CharField(blank=True, max_length=20, verbose_name='Celular')),
                ('office_number', models.CharField(blank=True, max_length=20, verbose_name='Tel\xe9fono de Oficina')),
                ('extension_number', models.CharField(blank=True, max_length=10, verbose_name='N\xfamero de Extensi\xf3n')),
                ('last_edit_date', models.DateTimeField(auto_now_add=True)),
                ('register_date', models.DateField(default=datetime.date.today)),
                ('bank_account_name', models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Nombre del Titular')),
                ('bank_account', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Cuenta Bancaria')),
                ('employer_registration_number', models.CharField(blank=True, default='', max_length=24, null=True, verbose_name='N\xfamero de Registro Patronal')),
                ('services', tinymce.models.HTMLField(blank=True, max_length=4096, null=True, verbose_name='Servicios que presta')),
                ('tax_person_type', models.CharField(choices=[('f', 'F\xedsica'), ('m', 'Moral')], default='m', max_length=1, verbose_name='Tipo de Persona')),
                ('status', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estatus')),
                ('type', models.IntegerField(choices=[(0, 'Proveedor'), (1, 'Acreedor'), (2, 'Tercero')], default=0, verbose_name='Tipo')),
                ('accounting_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Account', verbose_name='Cuenta Contable')),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Bank', verbose_name='Banco')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Pais', verbose_name='Pa\xeds')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Estado', verbose_name='Estado')),
                ('town', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='estado', on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Aliado Comercial',
                'verbose_name_plural': 'Aliado Comercial',
            },
        ),
        migrations.CreateModel(
            name='CommercialAllyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('rfc', models.CharField(max_length=20, verbose_name='RFC')),
                ('street', models.CharField(max_length=255, verbose_name='Calle')),
                ('outdoor_number', models.CharField(max_length=10, verbose_name='No. Exterior')),
                ('indoor_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='No. Interior')),
                ('colony', models.CharField(max_length=255, verbose_name='Colonia')),
                ('zip_code', models.CharField(max_length=5, verbose_name='C\xf3digo Postal')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Tel\xe9fono Principal')),
                ('secondary_number', models.CharField(blank=True, max_length=20, verbose_name='Tel\xe9fono Secundario')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('is_legal_representative', models.BooleanField(default=False, verbose_name='Es Representante Legal')),
                ('commercialally', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.CommercialAlly', verbose_name='Aliado Comercial')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Pais', verbose_name='Pa\xeds')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Estado', verbose_name='Estado')),
                ('town', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='estado', on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='FiscalPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounting_year', models.IntegerField(verbose_name='Ejercicio Contable')),
                ('account_period', models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], default=1, verbose_name='Mes')),
                ('status', models.IntegerField(choices=[(1, 'Abierto'), (2, 'Cerrado'), (3, 'Auditado')], default=1, verbose_name='Estatus')),
            ],
            options={
                'verbose_name': 'A\xf1o Contable',
                'verbose_name_plural': 'A\xf1os contables',
            },
        ),
        migrations.CreateModel(
            name='TypePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Tipo de P\xf3liza')),
                ('balanced_accounts', models.BooleanField(default=False, verbose_name='Cuadrar p\xf3liza')),
            ],
            options={
                'verbose_name': 'Tipo de P\xf3liza',
                'verbose_name_plural': 'Tipos de P\xf3liza',
            },
        ),
        migrations.AddField(
            model_name='accountingpolicy',
            name='fiscal_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.FiscalPeriod', verbose_name='Periodo Fiscal'),
        ),
        migrations.AddField(
            model_name='accountingpolicy',
            name='internal_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.InternalCompany', verbose_name='Empresa Interna'),
        ),
        migrations.AddField(
            model_name='accountingpolicy',
            name='type_policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.TypePolicy', verbose_name='Tipo de P\xf3liza'),
        ),
    ]
