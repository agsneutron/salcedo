# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-17 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assistance', '0004_assistancerecord_payroll_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistancerecord',
            name='absence',
            field=models.BooleanField(default=True, verbose_name='Ausente'),
        ),
    ]
