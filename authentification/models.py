from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    email = models.EmailField(
        gettext_lazy("email address"), blank=True, unique=True
    )
