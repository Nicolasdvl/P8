from django.test import Client, TestCase
from products.models import Product
from authentification.models import User


class TestProductsUrls(TestCase):
    """Test urls responses."""

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    @classmethod
    def setUpTestData(cls):
        """Initiate data for tests."""
        cls.product = Product.objects.get(id=1)
        cls.user = User.objects.get(id=1)

    def set_up(self):
        """Initiate django client test."""
        self.client = Client()

    def test_substitutes(self):
        """Test 'product/<int:id>' status."""
        context = {
            "product": self.product,
            "substitutes": self.product.get_subs_list(),
        }
        response = self.client.get("/product/1/", context)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        """Test 'product/<int:id>/details' status."""
        context = {"product": self.product}
        response = self.client.get("/product/1/details/", context)
        self.assertEqual(response.status_code, 200)

    def test_my_substitutes(self):
        """Test 'account/<int:id>/my_substitutes' status."""
        context = {"products": self.user.get_saves()}
        print(self.client.login(email="john@email.com", password="mdp"))
        self.client.login(email="john@email.com", password="mdp")
        response = self.client.get("account/1/my_substitutes", context)
        self.assertEqual(response.status_code, 200)
