from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin

from django_rolls.apps.users import urls as user_router_urls


api_endpoints = [
    path('', include(user_router_urls.api_urlpatterns)),
]

view_endpoints = [
    path('lk', include(user_router_urls.view_urlpatterns))
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(api_endpoints)), # API
    path('', include(view_endpoints)), # VIEW TEMPLATES

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
