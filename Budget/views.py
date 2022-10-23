from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from Budget.filter_backends import ShowOnlyOwnOrSharedBudgets, ShowOnlyOwnOrSharedExpensesAndIncome
from Budget.filtersets import BudgetFilter, IncomeFilter, ExpensesFilter
from Budget.models import Budget, Income, Expenses
from Budget.serializers import BudgetSerializer, IncomeSerializer, ExpensesSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, ShowOnlyOwnOrSharedBudgets]
    filterset_class = BudgetFilter


class IncomeViewSet(ModelViewSet):
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
