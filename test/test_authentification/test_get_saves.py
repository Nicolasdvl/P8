from django.test import TestCase
from authentification.models import User
from products.models import Product


class TestAuthentificationModels(TestCase):

    fixtures = [
        "test_users.json",
        "test_products.json",
        "test_categories.json",
    ]

    def test_get_saves(self):
        user = User.objects.get(id=2)
        self.assertEqual(user.get_saves(), [Product.objects.get(id=2)])
