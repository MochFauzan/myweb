# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-06 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='github',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
