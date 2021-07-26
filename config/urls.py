"""
Django urls for config app.

Assign urls to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("products.urls")),
    path("", include("search.urls")),
    path("", include("authentification.urls")),
]
