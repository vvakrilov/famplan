from django.contrib.auth import models as models_auth
from django.core.validators import MinLengthValidator
from django.db import models


class AppUser(models_auth.AbstractBaseUser, models_auth.PermissionsMixin):
    USERNAME_MAX_LEN = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'username'


class UserProfile(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 25

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )
    surname = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )
    phone_number = models.BigIntegerField(
        null=True,
        blank=True,
    )
    date_of_birth
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def first_n_last_user_names(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_n_last_user_names
