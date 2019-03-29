# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('ph_no', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/photos')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('userdata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
