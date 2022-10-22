from django.db import models


class IncomeCategoryEnum(models.TextChoices):
    EARNED_INCOME = "earned_income"
    PORTFOLIO_INCOME = "portfolio_income"
    PASSIVE_INCOME = "passive_income"
    OTHER = "other"


class ExpensesCategoryEnum(models.TextChoices):
    HOUSING = "housing"
    TRANSPORTATION = "transportation"
    FOOD = "food"
    UTILITIES = "utilities"
    INSURANCE = "insurance"
    MEDICAL_HEALTHCARE = "medical_healthcare"
    SAVING = "saving"
    PERSONAL = "personal"
    OTHER = "other"
