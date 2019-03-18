# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0032_service_base_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='base_url',
        ),
    ]
