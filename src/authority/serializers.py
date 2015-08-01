from django.contrib.auth import models as auth_models
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer

from infrastructure import serializers


class PermissionSerializer(BulkSerializerMixin, serializers.DynamicFieldsSerializer):
    class Meta:
        model = auth_models.Permission
        list_serializer_class = BulkListSerializer


class GroupSerializer(BulkSerializerMixin, serializers.DynamicFieldsSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta(object):
        model = auth_models.Group
        list_serializer_class = BulkListSerializer


class UserSerializer(BulkSerializerMixin, serializers.DynamicFieldsSerializer):
    class Meta(object):
        model = auth_models.User
        list_serializer_class = BulkListSerializer

        exclude = ('password',)
        read_only_fields = (
            'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'groups', 'user_permissions',)


class ProfileSerializer(serializers.DynamicFieldsSerializer):
    class Meta:
        model = auth_models.User
