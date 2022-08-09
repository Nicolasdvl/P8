"""
Django urls for core app.

Assign urls to views.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("legalnotice", views.legal, name="legal"),
    path("contact", views.contact, name="contact")
]
