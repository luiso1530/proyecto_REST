# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemareservas', '0008_auto_20170126_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservaciones',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='reservaciones',
            name='restaurantes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombres', to='sistemareservas.Restaurantes'),
        ),
    ]