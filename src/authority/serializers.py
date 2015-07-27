from django.contrib.auth import models as auth_models

from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer


class GroupSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = auth_models.Group
        list_serializer_class = BulkListSerializer


class UserSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = auth_models.User
        list_serializer_class = BulkListSerializer

        fields = ('id', 'username', 'email', 'is_active', 'date_joined', 'last_login', 'groups',)


class PermissionSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = auth_models.Permission
        list_serializer_class = BulkListSerializer
