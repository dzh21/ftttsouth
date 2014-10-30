from django.conf.urls import patterns, include, url

from tasks42 import views

urlpatterns = patterns('',
    url(r'^$', views.index),
)
