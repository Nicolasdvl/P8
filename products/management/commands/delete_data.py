from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            product.delete()
        categories = Category.objects.all()
        for category in categories:
            category.delete()