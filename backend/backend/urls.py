from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

import image_handle.views as image

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    url(r'^api/image/', include('image_handle.urls')),
    url(r'^api/profiles/', include('custom_profile.urls')),
    # swagger ui
    url(r'^swagger(?P<fm>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)