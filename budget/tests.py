import pytest
import requests

from budget.enums import ExpensesCategoryEnum, IncomeCategoryEnum
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


def test_add_expense(create_budget):
    created_budget_url = create_budget["url"]
    budget_id = int(created_budget_url.split("/")[-2])
    expense_data = {"category": ExpensesCategoryEnum.SAVING, "amount": 950.21, "budget": budget_id}

    response = requests.post(expenses_url, json=expense_data, **admin_credentials)
    assert response.status_code == 201
    response = response.json()
    assert expense_data["category"] == response["category"]
    assert float(expense_data["amount"]) == float(response["amount"])
    assert expense_data["budget"] == response["budget"]


def test_add_expense_with_incorrect_category(create_budget):
    created_budget_url = create_budget["url"]
    budget_id = int(created_budget_url.split("/")[-2])
    expense_data = {"category": "incorrect_category", "amount": 950.21, "budget": budget_id}

    response = requests.post(expenses_url, json=expense_data, **admin_credentials)
    assert response.status_code == 400
    assert response.json() == {"category": ['"incorrect_category" is not a valid choice.']}


def test_filtering_expense(create_budget):
    created_budget_url = create_budget["url"]
    budget_id = int(created_budget_url.split("/")[-2])
    expense_data_1 = {"category": ExpensesCategoryEnum.SAVING, "amount": 950.21, "budget": budget_id}
    expense_data_2 = {"category": ExpensesCategoryEnum.PERSONAL, "amount": 950.21, "budget": budget_id}

    response_1 = requests.post(expenses_url, json=expense_data_1, **admin_credentials)
    assert response_1.status_code == 201
    response_1 = response_1.json()

    response_2 = requests.post(expenses_url, json=expense_data_2, **admin_credentials)
    assert response_2.status_code == 201
    response_2 = response_2.json()

    response = requests.get(f"{expenses_url}?category={ExpensesCategoryEnum.SAVING}", **admin_credentials)
    assert response.status_code == 200
    response = response.json()

    responses_url = [expense["url"] for expense in response["results"]]
    assert response_1["url"] in responses_url
    assert response_2["url"] not in responses_url
