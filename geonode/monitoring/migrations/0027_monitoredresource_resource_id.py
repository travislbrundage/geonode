# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-26 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0026_auto_20190821_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoredresource',
            name='resource_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
