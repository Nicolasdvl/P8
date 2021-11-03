from django.test import TestCase
from products.models import Product


class TestSubstitutes(TestCase):
    """Test 'Product.get_sub_list()'."""

    fixtures = [
        "test_categories.json",
        "test_products.json",
        "test_users.json",
    ]

    def setUp(self):
        """Initiaise objects for tests."""
        self.cocazero = Product.objects.get(id=1)
        self.coca = Product.objects.get(id=3)
        self.perrier = Product.objects.get(id=2)
        self.pizza = Product.objects.get(id=4)
        self.pepsimax = Product.objects.get(id=5)

    def test_cocazero_return_pepsimax(self):
        """'perrier' share category with 'coca zero' and has better score."""
        self.assertIn(self.pepsimax, self.cocazero.get_subs_list())

    def test_cocazero_not_return_pizza(self):
        """'pizza' and 'cocazero' doesn't have category in common."""
        self.assertNotIn(self.pizza, self.cocazero.get_subs_list())

    def test_cocazero_not_return_coca(self):
        """'coca' share category with 'cocazero' but has lesser score."""
        self.assertNotIn(self.coca, self.cocazero.get_subs_list())
