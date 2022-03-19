from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Incomes(models.Model):
    INCOME_TYPE = 100

    income = models.PositiveIntegerField()
    income_type = models.TextField(max_length=INCOME_TYPE, )
    # author_name = models.

    funds_sum = models.BooleanField(default=False)
    object = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Expenses(models.Model):
    pass


class Schedule(models.Model):
    pass


class Statistics(models.Model):
    pass
