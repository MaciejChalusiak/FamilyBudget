import pytest
import requests

from budget.enums import IncomeCategoryEnum
from common.tests_fixtures.fixtures import admin_credentials, admin_id, base_url

budgets_url = f"{base_url}/budgets/"
incomes_url = f"{base_url}/incomes/"
expenses_url = f"{base_url}/expenses/"


@pytest.fixture
def create_budget():
    budget_data = {
        "owner": admin_id,
        "name": "New budget name",
    }
    response = requests.post(budgets_url, json=budget_data, **admin_credentials)
    assert response.status_code == 201
    return response.json()


def test_creating_budget():
    budget_data = {
        "owner": admin_id,
        "name": "New budget name",
    }
    response = requests.post(budgets_url, json=budget_data, **admin_credentials)
    assert response.status_code == 201
    created_budget_url = response.json()["url"]

    response = requests.get(created_budget_url, **admin_credentials)
    assert response.status_code == 200
    response = response.json()

    assert response["owner"] == budget_data["owner"]
    assert response["name"] == budget_data["name"]


def test_add_income(create_budget):
    created_budget_url = create_budget["url"]
    budget_id = int(created_budget_url.split("/")[-2])
    income_data = {"category": IncomeCategoryEnum.EARNED_INCOME, "amount": 1000.00, "budget": budget_id}

    response = requests.post(incomes_url, json=income_data, **admin_credentials)
    assert response.status_code == 201
    response = response.json()
    assert income_data["category"] == response["category"]
    assert float(income_data["amount"]) == float(response["amount"])
    assert income_data["budget"] == response["budget"]
