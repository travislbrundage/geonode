# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_client', '0002_auto_20180412_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='jumbotron_welcome_hide',
            field=models.BooleanField(default=False),
        ),
    ]
