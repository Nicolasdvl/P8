from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from products.models import Product, Category
from off.off_parser import Parser
from progress.spinner import PieSpinner


class Command(BaseCommand):
    def handle(self, *args, **options):
        parser = Parser()
        products = parser.main()
        spinner = PieSpinner("Insertion des données...", suffix=" ")
        for product_code in products:
            product = products[product_code]
            insertion_error = self.insert_products(product_code, product)
            if insertion_error:
                continue
            categories_list = product.get("categories")
            self.insert_categories(categories_list)
            for category in categories_list:
                self.insert_product_categories(product_code, category)
            spinner.next()
        spinner.finish()

    def insert_products(self, code: int, product: dict):
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
                nutriscore=nutriscore.upper(),
                image=image,
            )
            add.save()
        except IntegrityError:
            return True
        else:
            return False

    def insert_categories(self, categories_list: list):
        for category in categories_list:
            try:
                row = Category.objects.get(name=category)
            except Category.DoesNotExist:
                add = Category(name=category)
                add.save()

    def insert_product_categories(self, product_code: int, category: str):
        product = Product.objects.get(id=product_code)
        category = Category.objects.get(name=category)
        product.categories.add(category.id)
