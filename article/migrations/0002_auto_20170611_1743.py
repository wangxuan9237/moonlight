# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='column',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]