from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetup(APITestCase):
    def setUp(self):
        # urls
        self.registeration_url = reverse("register")
        self.login_url = reverse("login")
        self.refresh_token_url = reverse("token_refresh")
        self.create_post_url = reverse("create_post")
        # test data
        self.user_data = {"username": "test", "password": "test"}
        self.post_data = {"title": "Sample title", "content": "Sample content"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
