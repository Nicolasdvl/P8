"""
Django form for authentification app.

Python class to build a form.
"""
from django import forms


class LoginForm(forms.Form):
    """Declaration of form fields to build a login form."""

    email = forms.EmailField(
        label="E-mail ", widget=forms.TextInput(
            attrs={"id": "email", "class": "login-form"}
            )
    )
    password = forms.CharField(
        label="Mot de passe ", widget=forms.PasswordInput(
            attrs={"id": "password", "class": "login-form"}
            )
    )
