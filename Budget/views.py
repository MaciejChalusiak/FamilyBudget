from rest_framework.viewsets import ModelViewSet
from Budget.models import Budget, Income
from Budget.serializers import BudgetSerializer, IncomeSerializer
from rest_framework.permissions import IsAuthenticated


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

