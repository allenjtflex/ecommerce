# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-17 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170317_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]