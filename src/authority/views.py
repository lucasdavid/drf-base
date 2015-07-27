from django.contrib.auth import models as auth_models

from infrastructure import views

from . import serializers


class UsersViewSet(views.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer


class GroupsViewSet(views.ModelViewSet):
    queryset = auth_models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PermissionsViewSet(views.ModelViewSet):
    queryset = auth_models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
