from django.conf.urls import url
from . import views

urlpatterns = [
    url('^[/]?$', views.HomeView.as_view()),
    url('^docs[/]?$', views.DocsView.as_view()),
]
