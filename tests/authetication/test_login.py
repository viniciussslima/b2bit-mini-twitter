from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
import json
from rest_framework import status

from ..helpers import create_user

URL = reverse("authentication:login")


class LoginUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginUrlTest, cls).setUpClass()

    def setUp(self):
        self.client = APIClient()
        self.user = create_user()

    def test_login_complete(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "password": "password",
                }
            ),
            content_type="application/json",
        )

        self.assertDictContainsSubset(response.data["user"], self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_user(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "user",
                    "password": "password",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_invalid_password(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "password": "test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
