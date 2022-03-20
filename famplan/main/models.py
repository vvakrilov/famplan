from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Incomes(models.Model):
    INC_DICT = {
        'VER_STR': "Type of income:",
        'LEN': 100,
    }

    income = models.PositiveIntegerField(
        default=0,
    )
    income_type = models.CharField(
        verbose_name=INC_DICT['VER_STR'],
        max_length=INC_DICT['LEN'],
    )
    pay_day = models.DateTimeField()
    object = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Expenses(models.Model):
    pass


class Schedule(models.Model):
    pass


class Statistics(models.Model):
    pass
