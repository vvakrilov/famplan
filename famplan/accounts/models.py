from django.contrib.auth import models as models_auth
from django.core.validators import MinLengthValidator
from django.db import models

from famplan.common.validators import validate_only_letters


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
            validate_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name='Enter your first name'
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name='Enter your last name'
    )
    phone_number = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name='Enter your phone number'
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Enter your birth date'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='Enter email'
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_deleted = models.BooleanField(
        default=False,
    )

    @property
    def usernames(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.usernames

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        return self.save()
