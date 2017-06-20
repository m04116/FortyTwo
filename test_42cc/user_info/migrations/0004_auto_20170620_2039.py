# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0003_userinformation_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='height_field',
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='width_field',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='photo',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='user_photo/', width_field='width_field'),
        ),
    ]