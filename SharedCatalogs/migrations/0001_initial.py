# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=0, default=0, max_digits=25, verbose_name='N\xfamero de Cuenta')),
                ('name', models.CharField(max_length=500, verbose_name='Nombre de la Cuenta')),
                ('status', models.IntegerField(choices=[(1, 'Activa'), (2, 'Inactiva')], default=1, verbose_name='Estatus')),
                ('nature_account', models.IntegerField(choices=[(1, 'Deudora'), (2, 'Acreedora')], default=1, verbose_name='Naturaleza de Cuenta')),
                ('type_account', models.CharField(choices=[('A', 'Acumulativa'), ('D', 'Detalle')], max_length=1, verbose_name='Tipo de Cuenta')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2512, verbose_name='Nombre')),
                ('accounting_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Account', verbose_name='Cuenta Contable')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEstado', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupingCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0, null=True, verbose_name='Nivel')),
                ('grouping_code', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='C\xf3digo Agrupador')),
                ('account_name', models.CharField(max_length=500, verbose_name='Nombre de la Cuenta y/o subcuenta')),
            ],
            options={
                'verbose_name': 'C\xf3digo Agrupador de Cuentas del SAT.',
                'verbose_name_plural': 'C\xf3digo Agrupador de Cuentas del SAT.',
            },
        ),
        migrations.CreateModel(
            name='InternalCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Empresa Interna',
                'verbose_name_plural': 'Empresas Internas',
            },
        ),
        migrations.CreateModel(
            name='ItemAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(verbose_name='clave')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Rubro')),
            ],
            options={
                'verbose_name': 'Rubro',
                'verbose_name_plural': 'Rubros',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMunicipio', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePais', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Pa\xedses',
            },
        ),
        migrations.CreateModel(
            name='SATBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=3, verbose_name='Clave Cuenta SAT')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Cuenta SAT')),
                ('business_name', models.CharField(max_length=500, verbose_name='Raz\xf3n social')),
            ],
            options={
                'verbose_name': 'Bancos del SAT.',
                'verbose_name_plural': 'Bancos del SAT.',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Pais'),
        ),
        migrations.AddField(
            model_name='bank',
            name='sat_bank',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.SATBank', verbose_name='Banco del SAT'),
        ),
        migrations.AddField(
            model_name='account',
            name='grouping_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.GroupingCode', verbose_name='C\xf3digo Agrupador SAT'),
        ),
        migrations.AddField(
            model_name='account',
            name='internal_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.InternalCompany', verbose_name='Empresa Interna'),
        ),
        migrations.AddField(
            model_name='account',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.ItemAccount', verbose_name='Rubro de la Cuenta'),
        ),
        migrations.AddField(
            model_name='account',
            name='subsidiary_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SharedCatalogs.Account', verbose_name='Subcuenta de'),
        ),
    ]
