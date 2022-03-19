from django.urls import reverse
from rest_framework.test import APIClient
import json


def create_user():
    url = reverse("authentication:register")

    user = {
        "username": "test",
        "email": "test@test.com",
        "password": "password",
        "description": "test",
    }

    response = APIClient().post(
        url,
        json.dumps(user),
        content_type="application/json",
    )

    return response.data


def login_user(user):
    url = reverse("authentication:login")

    user["password"] = "password"

    response = APIClient().post(
        url,
        json.dumps(user),
        content_type="application/json",
    )

    return response.data


def create_and_login_user():
    user = create_user()

    return login_user(user)
