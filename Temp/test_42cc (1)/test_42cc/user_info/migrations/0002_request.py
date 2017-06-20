# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 15:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(default=datetime.date.today)),
                ('scheme', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=250)),
                ('content_type', models.CharField(max_length=250)),
                ('is_viewed', models.BooleanField(default=False)),
            ],
        ),
    ]