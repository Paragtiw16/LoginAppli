# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-13 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('username', models.CharField(blank=True, max_length=550, null=True)),
                ('password', models.CharField(blank=True, max_length=550, null=True)),
                ('email', models.EmailField(max_length=20, primary_key=True, serialize=False)),
                ('contactno', models.IntegerField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
