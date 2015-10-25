from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('friends.views',
	url(r'^$', 'index'),
	url(r'^add_friend/user=(?P<pk>\d+)/', 'add_friend'),
)