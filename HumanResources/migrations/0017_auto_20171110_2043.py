# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 20:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResources', '0016_auto_20171110_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': 'Banco', 'verbose_name_plural': 'Bancos'},
        ),
        migrations.RemoveField(
            model_name='payment_method',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='payment_method',
            name='name',
            field=models.CharField(default='Efectivo', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='registry_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 10, 20, 43, 6, 998236, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 10, 20, 43, 7, 32041, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='entry_time',
            field=models.TimeField(default=datetime.datetime(2017, 11, 10, 20, 43, 7, 32085, tzinfo=utc), verbose_name='Hora de Entrada'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='exit_time',
            field=models.TimeField(default=datetime.datetime(2017, 11, 10, 20, 43, 7, 32122, tzinfo=utc), verbose_name='Hora de Salida'),
        ),
    ]
