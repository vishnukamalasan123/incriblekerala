# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_hlist_destination_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='hlist',
            name='destination_details',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
