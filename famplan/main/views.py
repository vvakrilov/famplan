from django.shortcuts import render

from django.views import generic as view


# class UserRegistrationView()
class HomePage(view.TemplateView):
    template_name = 'base/temp-homepage.html'
