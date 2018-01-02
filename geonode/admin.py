# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.conf import settings

class GeonodeAdminSite(AdminSite):

    # The text to put at the top of each admin page, as an <h1> (a string).
    # By default, this is "Django administration".
    site_title = '%s %s' % (settings.SITENAME, ugettext_lazy('Administration'))

    # The text to put at the end of each admin page’s <title> (a string).
    # By default, this is "Django site admin".
    site_header = '%s %s' % (settings.SITENAME, ugettext_lazy('Administration'))

    # The text to put at the top of the admin index page (a string).
    # By default, this is "Site administration".
    index_title = '%s %s' % (settings.SITENAME, ugettext_lazy('Administration'))

admin_site = GeonodeAdminSite()