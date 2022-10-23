# Generated by Django 3.2.7 on 2022-10-22 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0003_budget_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='shared',
            field=models.ManyToManyField(blank=True, related_name='shared_budgets', to=settings.AUTH_USER_MODEL),
        ),
    ]