from rest_framework.viewsets import ModelViewSet
from Budget.models import Budget, Income, Expenses
from Budget.serializers import BudgetSerializer, IncomeSerializer, ExpensesSerializer
from rest_framework.permissions import IsAuthenticated
from Budget.filter_backends import ShowOnlyOwnBudgets


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [ShowOnlyOwnBudgets]


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]


class ExpensesViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAuthenticated]

