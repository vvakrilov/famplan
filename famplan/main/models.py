from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Object(models.Model):
    OBJECT_NAME = 50
    name = models.CharField(
        max_length=OBJECT_NAME
    )


class Incomes(models.Model):
    INCOME_TYPE = 100

    income_type = models.TextField(
        max_length=INCOME_TYPE
    )
    author_name = models.CharField(
        UserModel.first_name
    )
    author_phone = models.CharField(
        max_length=10
    )
    found = models.BooleanField(
        default=False
    )
    object = models.ForeignKey(Object, on_delete=models.CASCADE)


class Expenses(models.Model):
    pass


class Schedule(models.Model):
    pass


class Statistics(models.Model):
    pass
