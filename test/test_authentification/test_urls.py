from django.test import Client, TestCase


class TestAuthenticateUrls(TestCase):
    """Test urls from authentification app."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    def set_up(self):
        """Initiate django client test."""
        self.client = Client()
        self.valid_input = {
            "username": "Doe",
            "email": "doe@email.com",
            "password": "mdp",
            "confirme": "mdp",
        }

    def test_signup(self):
        """
        Test '/signup'.

        1/ GET response status should be 200.
        2/ POST response status with valid input should redirect at home page.
        Form errors are test in 'test_end_to_end' with selenium.
        """
        response = self.client.get("/signup")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/signup", self.valid_input)
        self.assertRedirects(response, "/")

    def test_login(self):
        """
        Test '/login'.

        1/ GET response status should be 200.
        2/ POST response status with valid input should redirect at home page.
        Form errors are test in 'test_end_to_end' with selenium.
        """
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/login", self.valid_input)
        self.assertRedirects(response, "/")

    def test_logout(self):
        """
        Test '/logout'.

        1/ GET response should redirect at home page.
        """
        response = self.client.get("/logout")
        self.assertRedirects(response, "/")

    def test_user(self):
        """Test '/user' status."""
        response = self.client.get("/account")
        self.assertEqual(response.status_code, 200)
        # Test GET status with auth user
        # Test GET status with unauth user
