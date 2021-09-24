from django.test import TestCase
from products.models import Product


class TestProductsModels(TestCase):

    fixtures = [
        "test_categories.json",
        "test_products.json",
        "test_users.json",
    ]

    def test_get_subs_list(self):
        product = Product.objects.get(id=3)
        self.assertEqual(product.get_subs_list(), [Product.objects.get(id=1)])
