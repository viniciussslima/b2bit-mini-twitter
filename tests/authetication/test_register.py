from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
import json
from rest_framework import status

URL = reverse("authentication:register")


class RegisterUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(RegisterUrlTest, cls).setUpClass()

    def setUp(self):
        self.client = APIClient()

    def test_register_complete(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "email": "test@test.com",
                    "password": "password",
                    "description": "test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_without_description(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "email": "test@test.com",
                    "password": "password",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_invalid_username(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "",
                    "email": "test@test.com",
                    "password": "password",
                    "description": "test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_email(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "email": "email",
                    "password": "password",
                    "description": "test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_password(self):
        response = self.client.post(
            URL,
            json.dumps(
                {
                    "username": "test",
                    "email": "email",
                    "password": "",
                    "description": "test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
