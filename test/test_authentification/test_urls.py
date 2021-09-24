from django.test import Client, TestCase


class TestAuthenticateUrls(TestCase):
    """Test urls responses."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    def set_up(self):
        """Initiate django client test."""
        self.client = Client()

    def test_signup(self):
        """Test '/signup' status."""
        response = self.client.get("/signup")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/login",
            {
                "username": "user",
                "email": "john@email.com",
                "password": "mdp",
                "confirme": "mdp",
            },
        )
        self.assertRedirects(response, "/")
        # missing test form errors

    def test_login(self):
        """Test '/login' status and redirect when user login."""
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/login", {"email": "john@email.com", "password": "mdp"}
        )
        self.assertRedirects(response, "/")
        # missing test form errors

    def test_logout(self):
        """Test '/logout' redirect."""
        response = self.client.get("/logout")
        self.assertRedirects(response, "/")

    def test_user(self):
        """Test '/user' status."""
        response = self.client.get("/user")
        self.assertEqual(response.status_code, 200)
