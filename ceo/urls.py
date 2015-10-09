from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from cms import views as cms_views
from schedule import views as schedule_views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^events/?$', schedule_views.calendar),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^$', cms_views.home),
    url(r'^(.*)$', cms_views.page),
)
