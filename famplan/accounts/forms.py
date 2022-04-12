from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from famplan.accounts.models import UserProfile
from famplan.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = UserProfile.first_name
    last_name = UserProfile.last_name
    date_of_birth = UserProfile.date_of_birth
    email = UserProfile.email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            surname=self.cleaned_data['surname'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'email',
        )


class DeleteProfileForm(DisabledFieldsFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    class Meta:
        model = UserProfile
        UserProfile.is_deleted = True
        fields = '__all__'
