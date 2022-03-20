from django.shortcuts import render

from django.views import generic as view


class HomePage(view.TemplateView):
    template_name = 'app-based/temp-homepage.html'
