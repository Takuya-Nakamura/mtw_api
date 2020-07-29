from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic

from .lib.views.classes import JsonView
from .lib.views.functions import  _hello_wold

# Create your views here.
class IndexView(generic.TemplateView):
    """
     top
    """

    template_name = "index.html"


#### views
class ClassApiView(JsonView):
    """
     original class base
    """

    def get(self, request, *args, **kwargs):
        json = self.echo_json()
        _hello_wold()
        return JsonResponse(self.echo_json())


def function_api(request):
    """
    function base
    """
    return JsonResponse({"name": "function base view"})


