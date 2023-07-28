from django.shortcuts import render
from django.views.generic import TemplateView
from .streets import Street

# Create your views here.


class IndexView(TemplateView):
    template_name = "generators/index.html"


def streetView(request):
    context = {"street": Street()}
    return render(request, template_name="generators/street.html", context=context)
