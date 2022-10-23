from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from budget.filter_backends import ShowOnlyOwnOrSharedBudgets, ShowOnlyOwnOrSharedExpensesAndIncome
from budget.filtersets import BudgetFilter, ExpensesFilter, IncomeFilter
from budget.models import Budget, Expenses, Income
from budget.serializers import BudgetSerializer, ExpensesSerializer, IncomeSerializer


class BudgetsViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ShowOnlyOwnOrSharedBudgets]
    filterset_class = BudgetFilter


class IncomesViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ShowOnlyOwnOrSharedExpensesAndIncome]
    filterset_class = IncomeFilter


class ExpensesViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ShowOnlyOwnOrSharedExpensesAndIncome]
    filterset_class = ExpensesFilter
