# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20190318_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='First_Name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Last_Name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='password2',
        ),
    ]
