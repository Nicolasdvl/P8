from django.test import Client, TestCase


class TestCoreUrls(TestCase):
    """Test urls responses."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    def set_up(self):
        """Initiate django client test."""
        self.client = Client()

    def test_index(self):
        """Test '/' status."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
