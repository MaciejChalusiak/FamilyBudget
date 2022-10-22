from django.db import models


class IncomeCategoryEnum(models.TextChoices):
    EARNED_INCOME = "earned_income"
    PORTFOLIO_INCOME = "portfolio_income"
    PASSIVE_INCOME = "passive_income"
    OTHER = "other"
