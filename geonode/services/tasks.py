# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings
from geonode.services.models import WebServiceHarvestLayersJob, WebServiceRegistrationJob
from geonode.services.views import update_layers, register_service_by_type
from geonode.people.models import Profile
from django.core.mail import send_mail


@periodic_task(run_every=crontab(minute=settings.SERVICE_UPDATE_INTERVAL))
def harvest_service_layers():
    if WebServiceHarvestLayersJob.objects.filter(status="process").count() == 0:
        for job in WebServiceHarvestLayersJob.objects.filter(status="pending"):
            try:
                job.status = "process"
                job.save()
                update_layers(job.service)
                job.delete()
            except Exception, e:
                print e
                job.status = 'failed'
                job.save()
                send_mail('Service harvest failed', 'Service %d failed, error is %s' % (job.service.id, str(e)),
                          settings.DEFAULT_FROM_EMAIL, [email for admin, email in settings.ADMINS], fail_silently=True)


@periodic_task(run_every=crontab(minute=settings.SERVICE_UPDATE_INTERVAL))
def import_service(job_id=None, owner='admin', name=None):
    boundsJobs = WebServiceRegistrationJob.objects.all()
    args = {'status': 'pending'}

    if job_id:
        args.update({'pk': job_id})

    response = {}
    for job in boundsJobs.filter(**args):
        try:
            job.status = "process"
            job.save()
            response = register_service_by_type(
                job.base_url, job.type, owner=Profile.objects.get(username=owner), name=name)
            job.status = "completed"
            job.result = response
            job.save()
            #job.delete()
        except Exception, e:
            job.status = 'failed'
            job.result = str(e)
            response.update({'error': str(e)})
            job.save()
            raise e

    return response