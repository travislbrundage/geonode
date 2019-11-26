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

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class FavoriteManager(models.Manager):

    def user_has_favorited_content_object(self, user, content_object):
        """
        if Favorite exists for input user and type and pk of the input
        content_object, return True.  else return False.
        impl note: can only be 0 or 1, per the class's unique_together.
        """
        content_type = ContentType.objects.get_for_model(type(content_object))
        result = self.filter(
            user=user,
            content_type=content_type,
            object_id=content_object.pk)

        if not result:
            return False
        else:
            return True

    def create_favorite(self, content_object, user):
        content_type = ContentType.objects.get_for_model(type(content_object))
        favorite, _ = self.get_or_create(
            user=user,
            content_type=content_type,
            object_id=content_object.pk,
        )
        return favorite


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete= models.CASCADE)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_on = models.DateTimeField(auto_now_add=True)

    objects = FavoriteManager()

    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'favorites'
        unique_together = (('user', 'content_type', 'object_id'),)

    def __unicode__(self):
        if self.content_object:
            return "Favorite: {}, {}, {}".format(
                self.content_object.title, self.content_type, self.user)
        else:
            return "Unknown"
