from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls


urlpatterns = [
    url('', include('home.urls')),
    url('^authority/', include('authority.urls')),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls'))
]
