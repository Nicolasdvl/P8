"""
Django urls for products app.

Assign urls to views.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("product/<int:id>/", views.substitutes, name="product_substitutes"),
    path("product/<int:id>/details/", views.details, name="product_details"),
    path(
        "account/my_substitutes/",
        views.my_substitutes,
        name="my_substitutes",
    ),
]
