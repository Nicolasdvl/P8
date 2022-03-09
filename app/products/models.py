"""
Django models for products app.

Contains the essential fields and behaviors of the data stored.
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """Models for table Category."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Allow objects display."""
        return self.name


class Product(models.Model):
    """Models for table Product."""

    NUTRISCORE = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("null", "unknow"),
    ]

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    brand = models.CharField(max_length=200)
    nutriscore = models.CharField(
        max_length=4, choices=NUTRISCORE, default="null"
    )
    image = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
    users_saves = models.ManyToManyField(User)

    def __str__(self):
        """Allow objects display."""
        return self.name

    def get_subs_list(self):
        """Return a list of the 6 more relevant substitutes."""
        categories = self.categories.all()
        categories_list = []
        for category in categories:
            categories_list.append(
                (len(category.product_set.all()), category.name)
            )
        categories_list.sort(key=self.sort_by_this, reverse=False)
        relevant_category = Category.objects.get(name=categories_list[0][1])
        products_list = []
        for product in relevant_category.product_set.all():
            if (
                product.name != self.name
                and product.nutriscore <= self.nutriscore
            ):
                products_list.append((product.nutriscore, product))
        products_list.sort(key=self.sort_by_this, reverse=False)
        substitutes = []
        for relevant in products_list[0:6]:
            substitutes.append(relevant[1])
        return substitutes

    def sort_by_this(self, element):
        """Use as key to sort elements in a list by the first value."""
        return element[0]
