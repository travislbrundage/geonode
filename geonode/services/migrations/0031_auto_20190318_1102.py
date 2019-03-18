# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0030_auto_20171212_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='base_url',
        ),
        migrations.AddField(
            model_name='service',
            name='wfs_url',
            field=models.URLField(db_index=True, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='wms_url',
            field=models.URLField(db_index=True, unique=True, null=True, blank=True),
        ),
    ]
