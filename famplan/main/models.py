from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Funds(models.Model):

    funds_amount = models.PositiveIntegerField(
        default=0,
    )
    date_added = models.DateTimeField()
    object = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Incomes(Funds):
    INCOMES = {
        'VERBOSE': "Type of income:",
        'LENGTH': 100,
    }
    funds_type = models.CharField(
        verbose_name=INCOMES['VERBOSE'],
        max_length=INCOMES['LENGTH'],
    )


class Expenses(Funds):
    EXPENSES = {
        'VERBOSE': "Type of expenses:",
        'LENGTH': 100,
    }
    funds_type = models.CharField(
        verbose_name=EXPENSES['VERBOSE'],
        max_length=EXPENSES['LENGTH'],
    )


class Schedule(models.Model):
    pass


class Statistics(models.Model):
    pass
