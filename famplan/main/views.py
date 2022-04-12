from django.views import generic as views

from famplan.main.models import Incomes, Expenses


class IndexPage(views.View):
    template_name = 'base/index.html'


class IncomesListView(views.View):
    model = Incomes
    template_name = 'base/dashboard.html'
    # queryset = model.object.all()
    context_object_name = 'incomes_list'
    paginate_by = 5


class ExpensesListView(views.View):
    model = Expenses
    template_name = 'base/expenses-list.html'
    # queryset = model.object.all()
    context_object_name = 'expenses_list'
    paginate_by = 5
