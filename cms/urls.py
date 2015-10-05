from django.conf.urls import patterns, include, url
from cms import views


urlpatterns = patterns('',
    url(r'^/$', views.home),
)
