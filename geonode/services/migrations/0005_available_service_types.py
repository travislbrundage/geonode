# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_job_result_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=4, choices=[(b'WMS', 'Web Map Service'), (b'REST', 'ArcGIS REST Service')]),
        ),
        migrations.AlterField(
            model_name='webserviceharvestlayersjob',
            name='status',
            field=models.CharField(default=b'pending', max_length=10, choices=[(b'pending', b'pending'), (b'failed', b'failed'), (b'process', b'process'), (b'completed', b'completed')]),
        ),
        migrations.AlterField(
            model_name='webserviceregistrationjob',
            name='status',
            field=models.CharField(default=b'pending', max_length=10, choices=[(b'pending', b'pending'), (b'failed', b'failed'), (b'process', b'process'), (b'completed', b'completed')]),
        ),
        migrations.AlterField(
            model_name='webserviceregistrationjob',
            name='type',
            field=models.CharField(max_length=4, choices=[(b'WMS', 'Web Map Service'), (b'REST', 'ArcGIS REST Service')]),
        ),
    ]
