from django.contrib.auth import views as view
from django.shortcuts import render

from famplan.accounts.models import FamilyUser


class UserLoginView(view.LoginView):
    model = FamilyUser
    

class UserProfileView(view.FormView):
    pass


class UserChangePasswordView(view.PasswordChangeView):
    pass


class UserLogOutView(view.LogoutView):
    pass
