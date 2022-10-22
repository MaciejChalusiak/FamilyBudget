from rest_framework.serializers import ModelSerializer, StringRelatedField
from Budget.models import Budget, Income


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ['url', 'category', 'amount', 'description', 'budget']


class BudgetSerializer(ModelSerializer):
    income = IncomeSerializer(many=True)

    class Meta:
        model = Budget
        fields = ['url', 'owner', 'name', 'income', 'income']
