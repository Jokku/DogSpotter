# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-27 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='ipaddress',
        ),
    ]