from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from products.models import Product, Category
from off.off_parser import Parser
from progress.bar import ChargingBar


class Command(BaseCommand):
    """Data insertion command for 'manage.py'."""

    def handle(self, *args, **options):
        """Insert products, categories and theirs relations in db."""
        parser = Parser()
        products = parser.main()
        bar = ChargingBar("Insertion des données...", max=len(products))
        for product_code in products:
            product = products[product_code]
            insertion_error = self.insert_products(product_code, product)
            if insertion_error:
                bar.next()
                continue
            categories_list = product.get("categories")
            self.insert_categories(categories_list)
            for category in categories_list:
                self.insert_product_categories(product_code, category)
            bar.next()
        bar.finish()

    def insert_products(self, code: int, product: dict) -> bool:
        """Return 'True' if product insertion failed."""
        code = code
        name = product.get("name")
        brand = product.get("brand")
        nutriscore = product.get("nutriscore")
        image = product.get("image")
        try:
            add = Product(
                id=code,
                name=name,
                brand=brand,
                nutriscore=nutriscore,
                image=image,
            )
            add.save()
        except IntegrityError:
            return True
        else:
            return False

    def insert_categories(self, categories_list: list):
        """Check if a category already exist in db before insertion."""
        for category in categories_list:
            try:
                Category.objects.get(name=category)
            except Category.DoesNotExist:
                add = Category(name=category)
                add.save()

    def insert_product_categories(self, product_code: int, category_name: str):
        """Add relation between a product and a category."""
        product = Product.objects.get(id=product_code)
        category = Category.objects.get(name=category_name)
        product.categories.add(category.id)
