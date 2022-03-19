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
