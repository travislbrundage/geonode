# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0031_auto_20190318_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='base_url',
            field=models.URLField(default=b'', unique=True, db_index=True),
        ),
    ]
