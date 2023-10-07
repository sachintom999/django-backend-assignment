from django.contrib.auth.models import User

from .test_setup import TestSetup


class TestViews(TestSetup):
    def activate_registered_user(self, username):
        """Helper method to active a registered user"""
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        return

    def register_and_login_user(self):
        """Helper method to register and login user returning tokens"""
        response = self.client.post(self.registeration_url, self.user_data)
        if response.status_code == 201:
            self.activate_registered_user(response.data["username"])

        res = self.client.post(self.login_url, self.user_data)
        return res.data["refresh"], res.data["access"]

    def test_user_cannot_register_without_data(self):
        """Test user registration failure without passing data"""
        res = self.client.post(self.registeration_url)
        self.assertEqual(res.status_code, 500)

    def test_user_can_register(self):
        """Test successful user registration"""
        res = self.client.post(self.registeration_url, self.user_data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            res.data,
            {
                "message": "User registered successfully",
                "username": self.user_data["username"],
            },
        )

    def test_user_login_failure(self):
        """Test login failure with invalid credentials"""
        response = self.client.post(self.registeration_url, self.user_data)
        if response.status_code == 201:
            self.activate_registered_user(response.data["username"])

        res = self.client.post(
            self.login_url, {"username": "test", "password": "wrong-password"}
        )
        self.assertEqual(res.status_code, 401)
        self.assertEqual(
            res.data,
            {"detail": "No active account found with the given credentials"},
        )

    def test_user_login_success(self):
        """Test successful user login"""
        response = self.client.post(self.registeration_url, self.user_data)
        if response.status_code == 201:
            self.activate_registered_user(response.data["username"])

        res = self.client.post(self.login_url, self.user_data)
        self.assertEqual(res.status_code, 200)
        self.assertIn("refresh", res.data)
        self.assertIn("access", res.data)

    def test_token_refresh(self):
        """Test token refresh to get a new access token"""
        refresh_token, access_token = self.register_and_login_user()
        res = self.client.post(
            self.refresh_token_url, {"refresh": refresh_token}
        )
        self.assertEqual(res.status_code, 200)
        # verify a new access token is received
        self.assertNotEqual(res.data["access"], access_token)

    def test_create_post_without_auth(self):
        """Test post creation failure without auth"""
        res = self.client.post(self.create_post_url, self.post_data)
        self.assertEqual(res.status_code, 401)

    def test_create_post_success(self):
        """Test successful post creation with auth"""
        refresh_token, access_token = self.register_and_login_user()
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        res = self.client.post(self.create_post_url, self.post_data, **headers)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["title"], self.post_data["title"])
        self.assertEqual(res.data["content"], self.post_data["content"])
