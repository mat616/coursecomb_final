# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 17:07
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='distribution',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='filter',
            name='must_courses',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='filter',
            name='must_dept',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='filter',
            name='time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
