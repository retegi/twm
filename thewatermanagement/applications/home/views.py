from django.shortcuts import render
#AÑADIDOS
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView
)


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home/index.html"
