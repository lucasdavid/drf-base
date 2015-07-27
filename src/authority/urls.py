from infrastructure.routers import Router

from . import views

r = Router()

r.register('users', views.UsersViewSet) \
    .register('groups', views.GroupsViewSet,
              base_name='user-groups',
              parents_query_lookups=['user'])

r.register('groups', views.GroupsViewSet) \
    .register('permissions', views.PermissionsViewSet,
              base_name='group-permissions',
              parents_query_lookups=['group'])


r.register('permissions', views.PermissionsViewSet)

urlpatterns = r.urls
