# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 05:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResources', '0004_auto_20171102_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='zip_code',
            field=models.CharField(default=0, max_length=5, verbose_name='C\xf3digo Postal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='registry_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 2, 5, 32, 31, 380955, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]