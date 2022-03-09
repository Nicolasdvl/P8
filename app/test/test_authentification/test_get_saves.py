from django.test import TestCase
from authentification.models import User
from products.models import Product


class TestAuthentificationModels(TestCase):
    """Test user model."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    def setUp(self):
        """Initiaise objects for tests."""
        self.cocazero = Product.objects.get(id=1)
        self.perrier = Product.objects.get(id=2)
        self.coca = Product.objects.get(id=3)
        self.pepsimax = Product.objects.get(id=5)

    def test_get_saves(self):
        """
        Test 'User.get_save()'.

        User has saved 'cocazero' and 'perrier' but hasn't saved 'coca'.
        """
        user = User.objects.get(id=2)
        self.assertIn(self.pepsimax, user.get_saves())
        self.assertIn(self.perrier, user.get_saves())
        self.assertNotIn(self.coca, user.get_saves())
