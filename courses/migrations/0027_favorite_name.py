# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_auto_20180430_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
