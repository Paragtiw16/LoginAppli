# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-13 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20180310_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
