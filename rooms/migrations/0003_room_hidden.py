# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20161217_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
