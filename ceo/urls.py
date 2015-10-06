from django.conf.urls import patterns, include, url
from django.contrib import admin

from cms import views as cms_views
from blog import views as blog_views
from schedule import views as schedule_views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/?$', blog_views.blog),
    url(r'^blog/tag/(.*)$', blog_views.blog_tag),
    url(r'^blog/[0-9]*\/[0-9]*\/(.*)', blog_views.blog_post),

    url(r'^events/?$', schedule_views.calendar),

    url(r'^$', cms_views.home),
    url(r'^(.*)$', cms_views.page),
)
