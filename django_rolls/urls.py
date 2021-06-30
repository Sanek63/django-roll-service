from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from django_rolls.apps.users import urls as user_router_urls


api_endpoint_view = [
    url(r'', include(user_router_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-token-auth/', views.obtain_auth_token), # AUTHORIZATION
    path('api/v1/', include(api_endpoint_view)), # API
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
