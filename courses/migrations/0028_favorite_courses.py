# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-01 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_favorite_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='courses',
            field=models.TextField(null=True),
        ),
    ]
