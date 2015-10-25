from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from user_profile.models import CofifiUser
from cofipy_app.models import QuoteIdea
from django.core.context_processors import request

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include("cofipy_app.urls")),
    url(r'^', include("friends.urls")),
    url(r'^messages/', include("message.urls")),
    url(r'^userprofile/', include("user_profile.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)