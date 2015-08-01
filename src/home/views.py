from django.http import HttpResponse
from django.template import loader, RequestContext
from rest_framework import views


class HomeView(views.View):
    def get(self, request):
        return HttpResponse(
            loader
                .get_template('index.html')
                .render(RequestContext(request)))


class DocsView(views.View):
    def get(self, request):
        return HttpResponse(
            loader
                .get_template('docs.html')
                .render(RequestContext(request)))