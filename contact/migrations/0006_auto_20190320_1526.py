# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20190320_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='message_1',
            field=models.TextField(max_length=2000),
        ),
    ]
