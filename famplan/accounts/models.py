from django.contrib.auth import models as models_auth
from django.core.validators import MinLengthValidator
from django.db import models

from famplan.accounts.managers import FamilyUserManager


class FamilyUser(models_auth.AbstractBaseUser, models_auth.PermissionsMixin):
    USERNAME_MAX_LEN = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'username'
    objects = FamilyUserManager()


class FamilyProfile(models.Model):
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

    user = models.OneToOneField(
        FamilyUser,
        on_delete=models.CASCADE,
        primary_key=True,

    )
