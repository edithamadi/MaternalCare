# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mama', '0005_auto_20181101_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='first_name',
            new_name='firspecialtyst_name',
        ),
    ]