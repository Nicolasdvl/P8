"""
Django models for authentification app.

Contains the essential fields and behaviors of the data stored.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from products.models import Product


class User(AbstractUser):
    """Custome user model."""

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(
        gettext_lazy("email address"), blank=True, unique=True
    )
    substitutes_saved = models.ManyToManyField(Product)

    def __str__(self):
        """Allow objects display."""
        return self.username

    def get_saves(self):
        """Return a list of all substitutes saved by an user."""
        my_substitutes = self.substitutes_saved.all()
        return my_substitutes
