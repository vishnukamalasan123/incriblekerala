# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]