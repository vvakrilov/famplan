from django.shortcuts import render

# Create your views here.
from django.views import generic as view


class TemporaryView(view.TemplateView):
    template_name = 'app-based/temp-test-page.html'
