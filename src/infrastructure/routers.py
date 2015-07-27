from rest_framework_bulk import routes
from rest_framework_extensions import routers


class Router(routers.ExtendedRouterMixin, routes.BulkRouter):
    pass
