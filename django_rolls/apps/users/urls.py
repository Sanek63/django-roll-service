from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from django_rolls.api.endpoint import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
