# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=20)),
                ('cantidad_personas', models.IntegerField()),
                ('hora', models.CharField(choices=[('1:00 pm', 'una'), ('2:00 pm', 'dos'), ('2:00 pm', 'tres')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('numero_tel', models.IntegerField()),
            ],
        ),
    ]
