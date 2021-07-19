from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class User(AbstractUser):

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=25)
    email = models.EmailField(
        gettext_lazy("email address"), blank=True, unique=True
    )
