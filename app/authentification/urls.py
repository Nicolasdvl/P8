"""
Django urls for authentification app.

Assign urls to views.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("account", views.user_page, name="account"),
]
