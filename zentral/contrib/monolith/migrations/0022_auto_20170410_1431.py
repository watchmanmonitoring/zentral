# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-10 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0021_auto_20170409_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifest',
            name='mbu_catalog',
        ),
        migrations.RemoveField(
            model_name='manifest',
            name='version',
        ),
        migrations.RemoveField(
            model_name='manifest',
            name='zentral_osquery',
        ),
        migrations.RemoveField(
            model_name='manifest',
            name='zentral_santa',
        ),
    ]
