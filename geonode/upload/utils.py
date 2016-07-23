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
from django.conf import settings
from geoserver.catalog import FailedRequestError
from geonode.geoserver.helpers import ogc_server_settings, gs_catalog
from geoserver.store import UnsavedDataStore
from xml.etree import ElementTree as ET

logger = logging.getLogger(__name__)


class UnsavedGeogigDataStore(UnsavedDataStore):
    save_method = "PUT"

    def __init__(self, catalog, name, workspace, author_name, author_email):
        self.author_name = author_name
        self.author_email = author_email
        super(UnsavedGeogigDataStore, self).__init__(catalog, name, workspace)

    def message(self):
        message = ET.Element('request')
        authorName = ET.SubElement(message, 'authorName')
        authorName.text = self.author_name
        authorEmail = ET.SubElement(message, 'authorEmail')
        authorEmail.text = self.author_email
        if settings.OGC_SERVER['default']['PG_GEOGIG'] is True:
            datastore = settings.OGC_SERVER['default']['DATASTORE']
            pg_geogig_db = settings.DATABASES[datastore]
            dbHost = ET.SubElement(message, 'dbHost')
            dbHost.text = pg_geogig_db['HOST']
            dbPort = ET.SubElement(message, 'dbPort')
            dbPort.text = str(pg_geogig_db.get('PORT', '5432'))
            dbName = ET.SubElement(message, 'dbName')
            dbName.text = pg_geogig_db['NAME']
            dbSchema = ET.SubElement(message, 'dbSchema')
            dbSchema.text = pg_geogig_db.get('SCHEMA', 'public')
            dbUser = ET.SubElement(message, 'dbUser')
            dbUser.text = pg_geogig_db['USER']
            dbPassword = ET.SubElement(message, 'dbPassword')
            dbPassword.text = pg_geogig_db['PASSWORD']
        else:
            parentDirectory = ET.SubElement(message, 'parentDirectory')
            parentDirectory.text = ogc_server_settings.GEOGIG_DATASTORE_DIR
        return ET.tostring(message)

    @property
    def href(self):
        return ("%sgeogig/repos/%s/init.json"
                % (ogc_server_settings.LOCATION, self.name))


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
            ds = UnsavedGeogigDataStore(
                cat, store_name, cat.get_default_workspace(),
                author_name, author_email)
            cat.save(ds)
            ds = cat.get_store(store_name)
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
