from django_filters import rest_framework as filters

from budget.models import Budget, Expenses, Income


class BudgetFilter(filters.FilterSet):
    class Meta:
        model = Budget
        fields = [
            "name",
        ]


class IncomeFilter(filters.FilterSet):
    budget_name = filters.Filter(field_name="budget__name")
    amount_gte = filters.Filter(field_name="amount", lookup_expr="gte")
    amount_lte = filters.Filter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Income
        fields = [
            "budget",
            "budget_name",
            "category",
        ]


class ExpensesFilter(filters.FilterSet):
    budget_name = filters.Filter(field_name="budget__name")
    amount_gte = filters.Filter(field_name="amount", lookup_expr="gte")
    amount_lte = filters.Filter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Expenses
        fields = [
            "budget",
            "budget_name",
            "category",
        ]
