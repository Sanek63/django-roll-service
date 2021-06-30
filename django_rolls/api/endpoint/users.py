from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
from django_rolls.apps.users.models import User
from django_rolls.api.serializer import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
