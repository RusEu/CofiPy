from django.conf.urls import patterns, include, url
from django.contrib import admin
#from .views import *

from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from cofipy_app import serializers

api = routers.DefaultRouter()

api.register(r'current_user', serializers.UserViewSet, base_name="current_user")
api.register(r'quote_ideas', serializers.QuoteViewSet)
api.register(r'cofifi_users', serializers.CofifiViewSet)

urlpatterns = patterns('cofipy_app.views',
	url(r'^$', 'index'),
	url(r'^homepage/', 'homepage'),
	url(r'^post/', 'post'),
	url(r'^search/', 'search'),
	url(r'^homepage/', 'homepage'),
	url(r'^send_coffee/(?P<pk>\d+)/', 'send_coffee'),
    url(r'^api', include(api.urls)),
)