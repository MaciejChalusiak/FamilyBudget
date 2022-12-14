from django.contrib.auth.models import User
from django.db import models

from budget.enums import ExpensesCategoryEnum, IncomeCategoryEnum


class Budget(models.Model):
    objects = models.Manager()

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_budgets")
    name = models.CharField(max_length=128)
    shared = models.ManyToManyField(User, related_name="shared_budgets", blank=True)


class Income(models.Model):
    objects = models.Manager()

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="income")
    category = models.CharField(choices=IncomeCategoryEnum.choices, max_length=128)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=256, null=True, blank=True)


class Expenses(models.Model):
    objects = models.Manager()

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    category = models.CharField(choices=ExpensesCategoryEnum.choices, max_length=128)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=256, null=True, blank=True)
