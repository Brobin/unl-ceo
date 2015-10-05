from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from blog import views


urlpatterns = patterns('',
    url(r'^$', views.blog),
    url(r'^tag/(.*)$', views.blog_tag),
    url(r'^[0-9]*\/[0-9]*\/(.*)/$', views.blog_post),
)
