# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_photo1_destination_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo1',
            name='admin_approved',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/images'),
            preserve_default=False,
        ),
    ]
