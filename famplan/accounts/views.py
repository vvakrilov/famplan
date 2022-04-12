from django.shortcuts import redirect, render

from famplan.accounts.models import UserProfile
from famplan.common.helpers import get_profile
from famplan.common.view_mixins import RedirectToDashboard
from django.views import generic as g_views
from famplan.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, get_user_model

from famplan.main.models import Incomes

UserModel = get_user_model()


class UserRegisterView(RedirectToDashboard, g_views.CreateView):
    form_class = CreateProfileForm
    template_name = 'profile/create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(g_views.DetailView):
    model = UserProfile
    template_name = 'profile/details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incomes = list(Incomes.objects.filter(user_id=self.object.user_id))

        income_funds = Incomes.objects \
            .filter(funds_amount__in=incomes) \
            .distinct()

        total_income = sum(v.funds_amount for v in income_funds)

        context.update({
            'incomes': incomes,
            'total_income': total_income,
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context


class EditProfileView(g_views.UpdateView):
    model = UserProfile
    form = EditProfileForm
    fields = '__all__'
    template_name = 'profile/edit.html'
    success_url = 'profile details'

    # def get_success_url(self):
    #     return reverse_lazy('profile details')


class DeleteProfileView(g_views.DeleteView):
    model = UserProfile
    form = DeleteProfileForm
    template_name = 'profile/delete.html'
    success_url = 'index'
