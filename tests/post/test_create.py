from urllib import response
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
import json
from rest_framework import status

from ..helpers import create_and_login_user

URL = reverse("post:create_post")


class CreateUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CreateUrlTest, cls).setUpClass()

    def setUp(self):
        response = create_and_login_user()

        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + response.get("tokens").get("access")
        )
        self.user = response.get("user")

    def test_create_complete(self):
        response = self.client.post(
            URL, json.dumps({"text": "test"}), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_text(self):
        response = self.client.post(
            URL, json.dumps({"text": ""}), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
