from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as models_auth

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
    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 25

    PARENT = 'Parent'
    KID = 'Kid'
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
    )

    user = models.OneToOneField(
        FamilyUser,
        on_delete=models.CASCADE,
        primary_key=True,

    )
