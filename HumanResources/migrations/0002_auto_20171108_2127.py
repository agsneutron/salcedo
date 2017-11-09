# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 21:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='registry_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 8, 21, 27, 25, 413267, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 8, 21, 27, 25, 456174, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='entry_time',
            field=models.TimeField(default=datetime.datetime(2017, 11, 8, 21, 27, 25, 456230, tzinfo=utc), verbose_name='Hora de Entrada'),
        ),
        migrations.AlterField(
            model_name='employeeassistance',
            name='exit_time',
            field=models.TimeField(default=datetime.datetime(2017, 11, 8, 21, 27, 25, 456274, tzinfo=utc), verbose_name='Hora de Salida'),
        ),
    ]
