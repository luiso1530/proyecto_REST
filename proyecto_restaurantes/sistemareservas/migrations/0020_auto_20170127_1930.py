# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemareservas', '0019_auto_20170127_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='hora',
            field=models.IntegerField(),
        ),
    ]
