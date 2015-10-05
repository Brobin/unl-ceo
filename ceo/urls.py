from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/?$', include('blog.urls')),
    url(r'^events/?$', include('schedule.urls')),
    url(r'^$', views.home),
    url(r'^(.*)$', views.page),
)
