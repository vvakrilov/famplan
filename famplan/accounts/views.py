from django.contrib.auth import views as view
from django.shortcuts import render
from django.views import generic_views

from famplan.accounts.models import FamilyUser
from famplan.common.view_mixins import RedirectToOverview


class UserRegistrationView(RedirectToOverview, generic_views.CreateView):
    form_class = CreateProfileForm
    template_name = ''


class UserLoginView(view.LoginView):
    model = FamilyUser


class UserProfileView(view.FormView):
    pass


class UserChangePasswordView(view.PasswordChangeView):
    pass


class UserLogOutView(view.LogoutView):
    pass
