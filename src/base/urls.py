from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url('', include('home.urls')),

    url('^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),

    url('^api/authority/', include('authority.urls')),
]
