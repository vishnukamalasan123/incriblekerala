# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_usercontinuation_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontinuation',
            name='username',
        ),
    ]
