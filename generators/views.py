from django.shortcuts import render
from django.views.generic import TemplateView
from .streets import Street
from .buildings import Building

# Create your views here.


class IndexView(TemplateView):
    template_name = "generators/index.html"


def streetView(request):
    context = {"street": Street()}
    return render(request, template_name="generators/street.html", context=context)


def buildingView(request):
    context = {"buildings": [Building("common"), Building("rare")]}
    return render(request, template_name="generators/building.html", context=context)
