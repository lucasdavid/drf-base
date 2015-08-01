from rest_framework_extensions import mixins
from rest_framework_bulk import BulkModelViewSet

from rest_framework import filters, permissions as rf_permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

from . import permissions


class GuardedModelViewSet(mixins.NestedViewSetMixin, BulkModelViewSet):
    permission_classes = (
        # TokenHasReadWriteScope,
        rf_permissions.DjangoModelPermissions,
    )
    filter_backends = (filters.DjangoFilterBackend,)


class IndividuallyGuardedModelViewSet(GuardedModelViewSet):
    permission_classes = (
        # TokenHasReadWriteScope,
        permissions.FullObjectPermissions,
    )
    filter_backends = (filters.DjangoFilterBackend, filters.DjangoObjectPermissionsFilter,)
