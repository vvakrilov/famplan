from django.shortcuts import render

from django import views

from . import models as fund_models


class IndexPage(views.View):
    template_name = 'templates/index.html'


class IncomesListView(views.View):
    model = fund_models.Incomes
    template_name = 'main/incomes-list.html'
    queryset = model.object.all()
    context_object_name = 'incomes_list'
    paginate_by = 5


class ExpensesListView(views.View):
    model = fund_models.Expenses
    template_name = 'main/expenses-list.html'
    queryset = model.object.all()
    context_object_name = 'expenses_list'
    paginate_by = 5


class FundsCalculationView(views.View):

    pass
