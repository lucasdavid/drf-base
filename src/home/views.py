from django.http import HttpResponse
from django.template import loader, RequestContext
from rest_framework import views


class HomeView(views.View):
    def get(self, request):
        template = loader.get_template('index.html')
        context = RequestContext(request)

        return HttpResponse(template.render(context))
