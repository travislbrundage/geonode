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
from simplejson import dumps

logger = logging.getLogger(__name__)


def create_geoserver_db_featurestore(
        store_type=None, store_name=None,
        author_name='admin', author_email='exchange@boundlessgeo.com'):
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
            rest_url = ogc_server_settings.LOCATION \
                + "geogig/repos/" + store_name + "/init.json"
            headers = {
                "Content-type": "application/json",
                "Accept": "application/json"
            }
            message = {
                "authorName": author_name,
                "authorEmail": author_email
            }
            if settings.PG_GEOGIG_DB is not None:
                message["dbHost"] = settings.PG_GEOGIG_DB['HOST']
                message["dbPort"] = settings.PG_GEOGIG_DB['PORT'] or '5432'
                message["dbName"] = settings.PG_GEOGIG_DB['NAME']
                message["dbSchema"] = settings.PG_GEOGIG_DB['SCHEMA']
                message["dbUser"] = settings.PG_GEOGIG_DB['USER']
                message["dbPassword"] = settings.PG_GEOGIG_DB['PASSWORD']
            else:
                message["parentDirectory"] = \
                    ogc_server_settings.GEOGIG_DATASTORE_DIR
            response = http.request(rest_url, 'PUT', dumps(message), headers)
            headers, body = response
            if 400 <= int(headers['status']) < 600:
                raise FailedRequestError(
                    "Error code (%s) from GeoServer: %s" %
                    (headers['status'], body))

            # TODO: Better way to do this?
            ds = None
            while ds is None:
                try:
                    ds = cat.get_store(store_name)
                except FailedRequestError:
                    ds = None
        else:
            logging.info(
                'Creating target datastore %s' % dsname)
            ds = cat.create_datastore(dsname)
            db = ogc_server_settings.datastore_db
            ds.connection_parameters.update(
                host=db['HOST'],
                port=db['PORT'] if isinstance(
                    db['PORT'], basestring) else str(db['PORT']) or '5432',
                database=db['NAME'],
                user=db['USER'],
                passwd=db['PASSWORD'],
                dbtype='postgis')
            cat.save(ds)
            ds = cat.get_store(dsname)
            assert ds.enabled

    return ds
