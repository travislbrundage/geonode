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

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from geonode.favorite.models import Favorite
from geonode.documents.models import Document
from geonode.layers.models import Layer
from geonode.maps.models import Map


def get_favorite_info(user, content_object):
    """
    return favorite info dict containing:
        a. an add favorite url for the input parameters.
        b. whether there is an existing Favorite for the input parameters.
        c. a delete url (if there is an existing Favorite).
    """
    result = {}

    url_content_type = type(content_object).__name__.lower()
    result["add_url"] = reverse("add_favorite_{}".format(url_content_type),
                                args=[content_object.pk])

    # Here is where that one model function is used
    existing_favorite = Favorite.objects.user_has_favorited_content_object(
        user, content_object)

    if existing_favorite:
        result["has_favorite"] = "true"
        result["delete_url"] = reverse("delete_favorite",
                                       args=[content_object.pk])
    else:
        result["has_favorite"] = "false"

    return result


def bulk_favorite_objects(user):
    """
    get the actual favorite objects for a user as a dict by content_type
    """
    favs = dict()
    for m in (Document, Map, Layer, get_user_model()):
        ct = ContentType.objects.get_for_model(m)
        favs[ct.name] = Favorite.objects.filter(user=user, content_type=ct)
    return favs
