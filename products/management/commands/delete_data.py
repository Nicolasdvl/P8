from django.core.management.base import BaseCommand
from products.models import Product, Category
from progress.bar import ChargingBar


class Command(BaseCommand):
    """Data deletion command for 'manage.py'."""

    def handle(self, *args, **options):
        """Remove products and categories from db."""
        products = Product.objects.all()
        categories = Category.objects.all()
        bar = ChargingBar(
            "Suppression des données... ",
            max=(len(products) + len(categories)),
        )
        for product in products:
            product.delete()
            bar.next()

        for category in categories:
            category.delete()
            bar.next()
        bar.finish()
