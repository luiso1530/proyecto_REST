# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_de_reservas', '0004_auto_20170127_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='dia',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
