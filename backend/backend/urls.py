from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from for_test import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^api/profiles/', include('custom_profile.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)