# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_delete_usercontinuation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
