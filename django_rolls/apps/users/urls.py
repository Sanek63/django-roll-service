from django.conf.urls import include, url
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django_rolls.api.endpoint import UserViewSet
from .views import lk

api_router = DefaultRouter()
api_router.register(r'users', UserViewSet)

api_urlpatterns = [
    url(r'^', include(api_router.urls)), # User view sets
    url(r'auth', views.obtain_auth_token) # User auth token
]

view_urlpatterns = [
    url('', lk)
]
