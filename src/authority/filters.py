import django_filters
from django.contrib.auth import models as auth_models


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = auth_models.User
        fields = ('username', 'email',)


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = auth_models.Group
        fields = ('name',)


class PermissionFilter(django_filters.FilterSet):
    class Meta:
        model = auth_models.Permission
        fields = ('name', 'codename', 'content_type',)
