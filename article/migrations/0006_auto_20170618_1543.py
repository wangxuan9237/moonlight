# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20170616_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-created',)},
        ),
    ]
