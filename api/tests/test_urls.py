from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_url(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
        }

        response = self.client.post(reverse("register"), data, format="json")

        # Check if the registration was successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_url(self):
        user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        data = {
            "username": "testuser",
            "password": "testpassword",
        }

        response = self.client.post(reverse("login"), data, format="json")

        # Check if the login was successful (status code 200) and if it returns an access token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_token_refresh_url(self):
        user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        login_data = {
            "username": "testuser",
            "password": "testpassword",
        }
        login_response = self.client.post(
            reverse("login"), login_data, format="json"
        )
        access_token = login_response.data["access"]
        refresh_token = login_response.data["refresh"]

        # Send a POST request to the token refresh URL with the access token
        refresh_data = {
            "refresh": refresh_token,
        }
        response = self.client.post(
            reverse("token_refresh"), refresh_data, format="json"
        )

        # Check if the token refresh was successful (status code 200) and if it returns a new access token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_create_post_url_unauthenticated(self):
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
        }

        response = self.client.post(
            reverse("create_post"), data, format="json"
        )

        # Check if the request is unauthorized (status code 401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
