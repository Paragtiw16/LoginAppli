# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-16 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxlogin', '0007_auto_20180314_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajaxlogin.Logins')),
            ],
        ),
    ]
