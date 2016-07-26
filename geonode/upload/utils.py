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

import logging
import os
from django.conf import settings
from geoserver.catalog import FailedRequestError
from geonode.geoserver.helpers import ogc_server_settings, gs_catalog
import httplib2
from urlparse import urlparse
import simplejson as json

logger = logging.getLogger(__name__)


def create_geoserver_db_featurestore(
        store_type=None, store_name=None,
        author_name='admin', author_email='admin@geonode.org'):
    cat = gs_catalog
    dsname = ogc_server_settings.DATASTORE
    # get or create datastore
    try:
        if store_type == 'geogig' and ogc_server_settings.GEOGIG_ENABLED:
            if store_name is not None:
                ds = cat.get_store(store_name)
            else:
                ds = cat.get_store(settings.GEOGIG_DATASTORE_NAME)
        elif dsname:
            ds = cat.get_store(dsname)
        else:
            return None
    except FailedRequestError:
        if store_type == 'geogig':
            if store_name is None and hasattr(
                    settings,
                    'GEOGIG_DATASTORE_NAME'):
                store_name = settings.GEOGIG_DATASTORE_NAME
            logger.info(
                'Creating target datastore %s' %
                store_name)
            if settings.OGC_SERVER['default']['PG_GEOGIG'] is True:
                username = ogc_server_settings.credentials.username
                password = ogc_server_settings.credentials.password
                url = ogc_server_settings.rest
                http = httplib2.Http(disable_ssl_certificate_validation=False)
                http.add_credentials(username, password)
                netloc = urlparse(url).netloc
                http.authorizations.append(
                    httplib2.BasicAuthentication(
                        (username, password),
                        netloc,
                        url,
                        {},
                        None,
                        None,
                        http
                    ))
                rest_url = ogc_server_settings.LOCATION + "geogig/repos/" \
                    + store_name + "/init"
                datastore = settings.OGC_SERVER['default']['DATASTORE']
                pg_geogig_db = settings.DATABASES[datastore]
                message = {
                    "authorName": author_name,
                    "authorEmail": author_email,
                    "dbHost": pg_geogig_db['HOST'],
                    "dbPort": pg_geogig_db.get('PORT', '5432'),
                    "dbName": pg_geogig_db['NAME'],
                    "dbSchema": pg_geogig_db.get('SCHEMA', 'public'),
                    "dbUser": pg_geogig_db['USER'],
                    "dbPassword": pg_geogig_db['PASSWORD']
                }
                headers = {
                    "Content-type": "application/json",
                    "Accept": "application/json"
                }
                response = http.request(rest_url, 'PUT',
                                        json.dumps(message), headers)
                headers, body = response
                if 400 <= int(headers['status']) < 600:
                    raise FailedRequestError(
                        "Error code (%s) from GeoServer: %s" %
                        (headers['status'], body))

                ds = cat.create_datastore(store_name)
                ds.type = "GeoGig"
                cat.save(ds)
                ds = cat.get_store(store_name)
            else:
                ds = cat.create_datastore(store_name)
                ds.type = "GeoGig"
                ds.connection_parameters.update(
                    geogig_repository=os.path.join(
                        ogc_server_settings.GEOGIG_DATASTORE_DIR,
                        store_name),
                    branch="master",
                    create="true")
                cat.save(ds)
                ds = cat.get_store(store_name)
        else:
            logging.info(
                'Creating target datastore %s' % dsname)
            ds = cat.create_datastore(dsname)
            db = ogc_server_settings.datastore_db
            ds.connection_parameters.update(
                host=db['HOST'],
                port=db['PORT'] or '5432',
                database=db['NAME'],
                user=db['USER'],
                passwd=db['PASSWORD'],
                dbtype='postgis')
            cat.save(ds)
            ds = cat.get_store(dsname)
            assert ds.enabled

    return ds
