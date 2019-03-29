# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='address',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='image',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='ph_no',
        ),
        migrations.AddField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='message',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
