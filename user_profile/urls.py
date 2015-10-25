from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('user_profile.views',
	url(r'^user=(?P<pk>\d+)/$', 'userprofile'),
)