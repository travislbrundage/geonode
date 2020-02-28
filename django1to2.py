#########################################################################
#
# Copyright (C) 2020 Planet Federal
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

import sys
import os

# This script doesn't check everything. For full list of deprecations and changes, check:
# https://docs.djangoproject.com/en/3.0/releases/2.0/
# General strategy:
# Check function for each deprecation in Django 2
# Check for most obvious case(s) and call it an error
# Check for less certain case(s) and call it a warning
# Report all of the above for each set of file contents given


def check_virtual_arguments(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, virtual_only in Field.contribute_to_class() and virtual in Model._meta.add_field()
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_enclosure(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, enclosure in SyndicationFeed.add_item()
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_callable_obj(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, callable_obj in assertRaisesMessage
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_include_app_name(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, app_name in include()
    include() also no longer supports 3-tuple (including admin.site.urls) as its first argument, not sure
    what that means or how to test
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_template_dirs(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, template_dirs in template loader functions:
    get_template(), cache_key(), get_template_sources()
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_host_asserts_redirects(content):
    """
    No instances found in GeoNode
    TODO: similar to Index() etc, host in assertRedirects
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_disconnect_weak(content):
    """
    Hard to check because disconnect is everywhere, but it doesn't look like it
    TODO: This is similar to the Index etc field
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    # Check for weak within disconnect( anywhere is fine
    # need the stack thing again
    maybe_deprecated_content = ["].reverse()",
                                "].last()"]
    warn_str = "WARNING: QuerySet reverse() and last() is not permitted after slicing. " \
               "Should be reordered to slice after calling reverse() or last()."
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_queryset_earliest(content):
    """
    No instances found in GeoNode
    TODO: This is similar to the Index etc field
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    maybe_deprecated_content = ["].reverse()",
                                "].last()"]
    warn_str = "WARNING: QuerySet reverse() and last() is not permitted after slicing. " \
               "Should be reordered to slice after calling reverse() or last()."
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_form_fields(content):
    """
    Forms - Seems to be no instances found in GeoNode
    Index - it seems like this isn't out there..?
    TODO: This, and copy this function but with Index, i.e. check_index
    For form fields, it's literally forms.<anything>(
    For index it's models.Index(
    There can be no positional arguments, i.e. all have to be defined explicitly with a <field>=
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    # if content has: forms.<anything>Field(, then everything between the open and close )
    # has to be defined as a specific variable in the pattern <var>=<val>
    # Step 1: Detect 'forms.<anything>Field(' within a string
    # Step 2: Grab all content up to matching ) - make sure it's the matching one!
    # This is done with a stack. Make a stack and if you find a (, push on stack. If you find a ),
    # pop the stack. If the stack is empty and you find a  ), we're done - that's all the content.
    # Step 3: Now we have some string with values in the field. Now we want to check positional arguments.
    # We don't necessarily care about anything other than outer content. Need yet another stack?
    # If we encounter any opening ( or [, push on to stack and read up until ) or ] empties the stack, discarding that
    deprecated_content = ["from django.core.urlresolvers import reverse"]
    maybe_deprecated_content = ["from django.core.urlresolvers import",
                                "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'reverse' import. Should be: from django.urls import reverse"
    warn_str = "WARNING: Possible deprecated 'reverse' import. Should be: from django.urls import reverse"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_queryset_slicing(content):
    """
    No instances in GeoNode (one instance was found in JS file which does not follow the same rules)
    TODO: Another version of this maybe for field_names no longer being accepted in earliest() and latest()?
    Check QuerySet slices aren't reverse()'d or last() since it no longer is accepted on sliced QuerySet
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    maybe_deprecated_content = ["].reverse()",
                                "].last()"]
    warn_str = "WARNING: QuerySet reverse() and last() is not permitted after slicing. " \
               "Should be reordered to slice after calling reverse() or last()."
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_use_for_related_fields(content):
    """
    Check for deprecated Manager.use_for_related_fields
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Manager.use_for_related_fields"]
    error_str = "ERROR: Found deprecated 'use_for_related_fields' property. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_escape_classes(content):
    """
    Check for deprecated escape classes
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["EscapeData", "EscapeBytes", "EscapeText", "EscapeString", "EscapeUnicode"]
    error_str = "ERROR: Found deprecated Escape class. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_escape(content):
    """
    Check for deprecated mark_for_escaping() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["mark_for_escaping()"]
    error_str = "ERROR: Found deprecated 'mark_for_escaping()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_filefield(content):
    """
    Check for deprecated get_directory_name() and get_filename() methods in FileField
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["FileField.get_directory_name()", "FileField.get_filename()"]
    maybe_deprecated_content = [".get_directory_name()", ".get_filename()"]
    error_str = "ERROR: Found deprecated 'get_directory_name()' or 'get_filename()' function. Should be removed"
    warn_str = "WARNING: Possible deprecated 'get_directory_name()' or 'get_filename()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_widget_format(content):
    """
    Check for deprecated _format_value() function in Widget
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Widget._format_value()"]
    maybe_deprecated_content = ["._format_value()"]
    error_str = "ERROR: Found deprecated '_format_value()' function. Should be removed"
    warn_str = "WARNING: Possible deprecated '_format_value()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_precision_wkt(content):
    """
    Check for deprecated precision_wkt() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["precision_wkt()"]
    error_str = "ERROR: Found deprecated 'precision_wkt()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_catalogs(content):
    """
    Check for deprecated javascript_catalog() and json_catalog() functions
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["javascript_catalog()", "json_catalog()"]
    error_str = "ERROR: Found deprecated 'javascript_catalog()' or 'json_catalog()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_virtual_fields(content):
    """
    Check for deprecated virtual_fields property
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = [".virtual_fields"]
    error_str = "ERROR: Found deprecated 'virtual_fields' property. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_time_functions(content):
    """
    Check for deprecated time functions
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["accessed_time(), created_time(), modified_time()"]
    error_str = "ERROR: Found deprecated time function. The following functions should be removed: " \
                "accessed_time(), created_time(), modified_time()"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_context_has_key(content):
    """
    Check for deprecated has_key() method in Context
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Context.has_key()"]
    maybe_deprecated_content = ["has_key()"]
    error_str = "ERROR: Found deprecated 'has_key()' Context method. Should be removed"
    warn_str = "WARNING: Possible deprecated 'has_key()' Context method. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_commaseparatedintegerfield(content):
    """
    Check for deprecated CommaSeparatedIntegerField
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["CommaSeparatedIntegerField"]
    error_str = "ERROR: Found deprecated 'CommaSeparatedIntegerField'. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_allow_lazy(content):
    """
    Check for deprecated allow_lazy() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["allow_lazy()"]
    error_str = "ERROR: Found deprecated 'allow_lazy()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_cascaded_union(content):
    """
    Check for deprecated cascaded_union property in MultiPolygon
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["MultiPolygon.cascaded_union"]
    maybe_deprecated_content = [".mime_type"]
    error_str = "ERROR: Found deprecated 'cascaded_union' attribute. Should be removed"
    warn_str = "WARNING: Possible deprecated 'cascaded_union' attribute. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if "from django.contrib.gis.geos import MultiPolygon" in content \
            or "from django.contrib.gis.geos import" in content:
        if all(x in content for x in maybe_deprecated_content):
            return [warn_str]
    return []


def check_geos_functions(content):
    """
    Check for deprecated functions from geos
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["get_srid()", "set_srid(", "get_x()", "set_x(", "get_y()", "set_y(", "get_z()", "set_z(",
                          "get_coords()", "set_coords"]
    error_str = "ERROR: Found deprecated geos function. The following functions are no longer supported " \
                "and should be removed: GEOSGeometry.get_srid(), GEOSGeometry.set_srid(), " \
                "Point.get_x(), Point.get_y(), Point.get_z(), Point.set_x(), Point.set_y(), Point.set_z(), " \
                "Point.get_coords(), Point.set_coords()"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_loader_origin(content):
    """
    Check for deprecated LoaderOrigin and StringOrigin in template loaders
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.template.loader import LoaderOrigin",
                          "from django.template.loader import StringOrigin"]
    maybe_deprecated_content = ["from django.template.loader import"]
    error_str = "ERROR: Found deprecated 'LoaderOrigin' or 'StringOrigin' import. Should be: 'Origin'"
    warn_str = "WARNING: Possible deprecated 'LoaderOrigin' or 'StringOrigin' import. Should be: 'Origin'"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_eggs_loader(content):
    """
    Check for deprecated eggs template loader, django.template.loaders.eggs.Loader
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.template.loaders.eggs import Loader"]
    maybe_deprecated_content = ["from django.template.loaders.eggs import",
                                "from django.template.loaders import eggs"]
    error_str = "ERROR: Found deprecated 'Loader' import. Should be removed"
    warn_str = "WARNING: Possible deprecated 'Loader' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_mime_type(content):
    """
    Check for deprecated mime_type attribute in Atom1Feed and RssFeed
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Atom1Feed.mime_type", "RssFeed.mime_type"]
    maybe_deprecated_content = [".mime_type"]
    error_str = "ERROR: Found deprecated 'mime_type' attribute. Should be removed"
    warn_str = "WARNING: Possible deprecated 'mime_type' attribute. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if "from django.utils.feedgenerator import Atom1Feed" in content \
            or "from django.utils.feedgenerator import RssFeed" in content \
            or "from django.utils.feedgenerator import" in content:
        if all(x in content for x in maybe_deprecated_content):
            return [warn_str]
    return []


def check_loader_call(content):
    """
    Check for deprecated Loader.__call__() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Loader.__call__()"]
    maybe_deprecated_content = ["__call__()"]
    error_str = "ERROR: Found deprecated '__call__()' Loader function. Should be removed"
    warn_str = "WARNING: Possible deprecated '__call__()' Loader function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if "from django.template.loaders.base import Loader" in content \
            or "from django.template.loaders.base import" in content:
        if all(x in content for x in maybe_deprecated_content):
            return [warn_str]
    return []


def check_load_template(content):
    """
    Check for deprecated load_template and load_template_sources methods
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["load_template", "load_template_sources"]
    error_str = "ERROR: Found deprecated 'load_template' or 'load_template_sources' method. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_geoip(content):
    """
    Check for deprecated geoip imports
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.contrib.gis import geoip"]
    maybe_deprecated_content = ["from django.contrib.gis import",
                                "geoip"]
    error_str = "ERROR: Found deprecated 'geoip' import. Should be removed"
    warn_str = "WARNING: Possible deprecated 'geoip' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_geomanager_geoqueryset(content):
    """
    Check for deprecated GeoManager and GeoQuerySet classes
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["GeoManager", "GeoQuerySet"]
    error_str = "ERROR: Found deprecated 'GeoManager' or 'GeoQuerySet' class. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_skip_if_customer_user(content):
    """
    Check for deprecated skipIfCustomUser() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["skipIfCustomUser"]
    error_str = "ERROR: Found deprecated 'skipIfCustomUser' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_lazy_relation(content):
    """
    Check for deprecated add_lazy_relation() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["add_lazy_relation"]
    error_str = "ERROR: Found deprecated 'add_lazy_relation' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_field_properties(content):
    """
    Check for deprecated rel, remote_field properties and _get_val_from_obj() function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["Field.rel", "Field.remote_field.to"]
    deprecated_function = ["Field._get_val_from_obj()"]
    error_str = "ERROR: Found deprecated 'Field.rel' or 'Field.remote_Field'. Should be removed"
    error_function = "ERROR: Found deprecated 'Field._get_val_from_obj()' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in deprecated_function):
        return [error_function]
    return []


def check_forms_extras(content):
    """
    Check for deprecated django.forms.extras import
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["django.forms.extras", "from django.forms import extras"]
    maybe_deprecated_content = ["from django import forms"]
    warn_str = "WARNING: Found deprecated use of 'django.forms.extras' reference. Should be removed"
    error_str = "ERROR: Found deprecated 'django.forms.extras' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    if all(x in content for x in maybe_deprecated_content):
        if 'forms.extras' in content:
            return [warn_str]
    return []


def check_aggregate_support(content):
    """
    Check for deprecated check_aggregate_support function
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["check_aggregate_support"]
    error_str = "ERROR: Found deprecated 'check_aggregate_support' function. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_xreadlines(content):
    """
    Check for deprecated HttpRequest.xreadlines() function calls
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["xreadlines"]
    error_str = "ERROR: Found deprecated 'xreadlines' HttpRequest function. " \
                "Should be removed in favor of iterating over the request."
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_default_content_type(content):
    """
    Check for deprecated DEFAULT_CONTENT_TYPE
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["DEFAULT_CONTENT_TYPE"]
    error_str = "ERROR: Found deprecated 'DEFAULT_CONTENT_TYPE' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_psycopg2(content):
    """
    Check for deprecated psycopg2 import
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    maybe_deprecated_content = ["postgresql_psycopg2"]
    warn_str = "WARNING: Found outdated 'postgresql_psycopg2' reference. If done as an import, it is deprecated. " \
               "Still valid for for the DATABASES setting. " \
               "Otherwise, should be 'from django.db.backends import postgresql'"
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_ogr_exception(content):
    """
    Check for deprecated OGRException
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["OGRException"]
    error_str = "ERROR: Found deprecated 'OGRException' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_base_expression(content):
    """
    Check for deprecated _output_field reference in BaseException
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["_output_field"]
    error_str = "ERROR: Found deprecated '_output_field' BaseException property. Should be 'output_field'"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_django_runtime(content):
    """
    Check for deprecated DjangoRuntimeWarning
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["DjangoRuntimeWarning"]
    error_str = "ERROR: Found deprecated 'DjangoRuntimeWarning' import. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_url_namespacing(content):
    """
    Check urls.py files have been namespaced with app_name
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    if "app_name" not in content:
        return ["ERROR: urls.py needs a defined 'app_name' within the file for correct namespacing in Django 2+. "
                "Add the app name to the beginning of the file as 'app_name = <name>'."]
    return []


def check_delete_cascading(content):
    """
    Check that ForeignKey and OneToOne model relations have explicitly defined on_delete=models.CASCADE
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    if content.count("ForeignKey") + content.count("OneToOne") > content.count("on_delete=models.CASCADE"):
        return ["ERROR: Found model fields ForeignKey or OneToOne without 'on_delete=models.CASCADE'. "
                "This must be explicitly specified in Django 2+."]
    return []


def check_assignment_tag(content):
    """
    Check for deprecated assignment_tag
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["assignment_tag"]
    error_str = "ERROR: Found deprecated 'assignment_tag'. Should be 'simple_tag'"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_session_authentication(content):
    """
    Check for deprecated session authentication middleware
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["SessionAuthenticationMiddleware"]
    error_str = "ERROR: Found deprecated 'SessionAuthenticationMiddleware'. Should be removed"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_user_properties(content):
    """
    Check for deprecated user functions
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["is_authenticated()", "is_anonymous()"]
    error_str = "ERROR: Found deprecated User function (is_authenticated or is_anonymous). Should be: 'MIDDLEWARE'"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_render(content):
    """
    Check for deprecated render imports
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    # Note: render_to_response methods still exist in a valid way on generic views
    maybe_deprecated_content = ["render_to_response"]
    warn_str = "WARNING: Potentially deprecated 'render_to_response' import. Should be: 'render'"
    if all(x in content for x in maybe_deprecated_content):
        return [warn_str]
    return []


def check_middleware(content):
    """
    Check for deprecated middleware definition
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["MIDDLEWARE_CLASSES"]
    error_str = "ERROR: Found deprecated 'MIDDLEWARE_CLASSES'. Should be: 'MIDDLEWARE'"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_urlresolvers(content):
    """
    Check for deprecated urlresolvers imports
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    deprecated_content = ["from django.core.urlresolvers import", "from django.core import urlresolvers"]
    error_str = "ERROR: Found deprecated 'urlresolvers' import. Should be: from django.urls import"
    if all(x in content for x in deprecated_content):
        return [error_str]
    return []


def check_for_problems(filename, content):
    """
    Checks for any content which is deprecated in Django 2
    :param content: str of content to screen for deprecations
    :return: str indicating probable errors or None
    """
    problems = []
    problems.extend(check_urlresolvers(content))
    problems.extend(check_middleware(content))
    problems.extend(check_render(content))
    problems.extend(check_user_properties(content))
    problems.extend(check_session_authentication(content))
    problems.extend(check_assignment_tag(content))
    problems.extend(check_delete_cascading(content))
    problems.extend(check_django_runtime(content))
    problems.extend(check_base_expression(content))
    problems.extend(check_ogr_exception(content))
    problems.extend(check_psycopg2(content))
    problems.extend(check_default_content_type(content))
    problems.extend(check_xreadlines(content))
    problems.extend(check_aggregate_support(content))
    problems.extend(check_forms_extras(content))
    problems.extend(check_field_properties(content))
    problems.extend(check_lazy_relation(content))
    problems.extend(check_skip_if_customer_user(content))
    problems.extend(check_geomanager_geoqueryset(content))
    problems.extend(check_geoip(content))
    problems.extend(check_load_template(content))
    problems.extend(check_loader_call(content))
    problems.extend(check_mime_type(content))
    problems.extend(check_eggs_loader(content))
    problems.extend(check_loader_origin(content))
    problems.extend(check_geos_functions(content))
    problems.extend(check_cascaded_union(content))
    problems.extend(check_allow_lazy(content))
    problems.extend(check_commaseparatedintegerfield(content))
    problems.extend(check_context_has_key(content))
    problems.extend(check_time_functions(content))
    problems.extend(check_virtual_fields(content))
    problems.extend(check_catalogs(content))
    problems.extend(check_precision_wkt(content))
    problems.extend(check_widget_format(content))
    problems.extend(check_filefield(content))
    problems.extend(check_escape(content))
    problems.extend(check_escape_classes(content))
    problems.extend(check_use_for_related_fields(content))
    if "urls.py" in filename:
        problems.extend(check_url_namespacing(content))
    return problems


allpyfiles = []
if len(sys.argv) > 1:
    # Check if arg is a python file
    if ".py" in sys.argv[1] and ".pyc" not in sys.argv[1] and ".py2" not in sys.argv[1] and ".py3" not in sys.argv[1]:
        allpyfiles.extend([sys.argv[1]])
    # TODO: Not super smart about dir arg it receives, can be improved
    # Not guaranteed to be a directory here still
    else:
        dirtouse = os.getcwd() + '/' + sys.argv[1]
        for (dirpath, dirnames, filenames) in os.walk(dirtouse):
            for f in filenames:
                if ".py" in f and ".pyc" not in f and ".py2" not in f and ".py3" not in f:
                    allpyfiles.extend([dirpath + '/' + f])

# TODO: Check contents of each file for problematic content
# TODO: We probably don't care about anything in the migrations directory either
print("========== BEGIN FILE ANALYSIS ==========")
for f in allpyfiles:
    print("---------- ANALYZING FILE: {0} ----------".format(f))
    file = open(f, "r")
    contents = file.read()
    problems = check_for_problems(f, contents)
    if problems:
        for p in problems:
            print(p)
    print("---------- COMPLETED EXAMINATION: {0} ----------".format(f))
print("========== FILE ANALYSIS COMPLETE ==========")

# TODO: See if we can reimplement checking the line number as well
'''
for f in allpyfiles:
    file = open(f, "r")
    lines = file.readlines()
    lineno = 1
    contents = ""
    for line in lines:
        problems = check_for_problems(line)
        if problems:
            print("L{0}: {1}".format(lineno, problems))
        # print("L{0}: {1}".format(lineno, line))
        lineno += 1
        contents += line
    # print("all content: {0}".format(contents))
    break
'''
