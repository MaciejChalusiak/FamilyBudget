import requests

from common.tests_fixtures.fixtures import admin_credentials, base_url

url = f"{base_url}/users/"

user_data = {"username": "new_user", "email": "new_user@mail.com", "password": "admin"}


def test_creating_user():
    response = requests.post(url, json=user_data)
    assert response.status_code == 201
    response = response.json()

    assert response["username"] == user_data["username"]
    assert response["email"] == user_data["email"]

    created_user_url = response["url"]
    response = requests.delete(created_user_url, auth=(user_data["username"], user_data["password"]))
    assert response.status_code == 204


def test_creating_user_with_already_existing_username():
    response = requests.get(f"{url}1", **admin_credentials)
    assert response.status_code == 200
    existing_username = response.json()["username"]

    existing_user_data = user_data.copy()
    existing_user_data["username"] = existing_username

    response = requests.post(url, json=existing_user_data)
    assert response.status_code == 400
    assert response.json() == {"username": ["A user with that username already exists."]}
