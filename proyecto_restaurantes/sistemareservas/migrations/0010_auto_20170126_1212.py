# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemareservas', '0009_auto_20170126_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='restaurantes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistemareservas.Restaurantes'),
        ),
    ]