from rest_framework.serializers import ModelSerializer
from budget.models import Budget, Income, Expenses
from user.serializers import ShowSharedUserSerializer


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ['url', 'category', 'amount', 'description', 'budget']


class ExpensesSerializer(ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['url', 'category', 'amount', 'description', 'budget']


class BudgetSerializer(ModelSerializer):
    income = IncomeSerializer(many=True, required=False)
    expenses = ExpensesSerializer(many=True, required=False)
    shared = ShowSharedUserSerializer(many=True, required=False)

    class Meta:
        model = Budget
        fields = ['url', 'owner', 'name', 'income', 'expenses', 'shared']
