# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemareservas', '0004_auto_20170126_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='dia',
            field=models.CharField(max_length=20),
        ),
    ]
