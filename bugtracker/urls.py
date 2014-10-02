# -*- coding: utf-8; -*-
#!/usr/bin/env python

__author__ = 'Olexander Yermakov'
__email__ = 'mannavard1611@gmail.com'


from django.conf.urls import patterns, include, url

from .views import BugListView
from .views import BugDetailView
from .views import RegisterView


urlpatterns = patterns('',
        url(r'^$', BugListView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', BugDetailView.as_view(), name='detail'),
        url(r'^register/$', RegisterView.as_view(), name='register'),
)
