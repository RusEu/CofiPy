from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('message.views',
	url(r'^all/$', 'index'),
	url(r'^friend=(?P<friend>\w+)$', 'friend_message'),
	url(r'^ajax/friend=(?P<friend>\w+)$', 'ajax'),
	url(r'^message/friend=(?P<friend>\w+)$', 'json_message'),
)