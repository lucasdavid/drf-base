from rest_framework_extensions import mixins
from rest_framework_bulk import BulkModelViewSet


class ModelViewSet(mixins.NestedViewSetMixin, BulkModelViewSet):
    pass
