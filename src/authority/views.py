from django.contrib.auth import models as auth_models
from infrastructure import views

from . import serializers, filters


class UsersViewSet(views.IndividuallyGuardedModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = filters.UserFilter


class GroupsViewSet(views.GuardedModelViewSet):
    queryset = auth_models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_class = filters.GroupFilter


class PermissionsViewSet(views.GuardedModelViewSet):
    queryset = auth_models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    filter_class = filters.PermissionFilter
