from django.contrib import admin
from guardian import admin as guardian_admin
from functools import partial


class GuardedModelAdminMixin(guardian_admin.GuardedModelAdminMixin):
    @property
    def queryset(self):
        return partial(self.get_queryset)


class GuardedModelAdmin(GuardedModelAdminMixin, admin.ModelAdmin):
    """Extend this class if your model is guarded by Guardian (per-object authorization).

    This class is a workaround for Django-1.8.
    See more at issue #307 https://github.com/django-guardian/django-guardian/issues/307
    """
