"""
Django form for authentification app.

Python class to build a form.
"""
from django import forms
from django.core.exceptions import ValidationError
from authentification.models import User


class SignupForm(forms.ModelForm):
    """Declaration of form fields to build a sign up form."""

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"id": "password"}),
    )
    confirme = forms.CharField(
        label="Confirme your password",
        widget=forms.PasswordInput(attrs={"id": "confirme"}),
    )

    class Meta:
        """Declare of form fields to build a sign up form."""

        model = User
        fields = ("username", "email", "password")

    def clean(self):
        """Declare of form fields to build a sign up form."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirme = cleaned_data.get("confirme")
        if password and confirme:
            if password != confirme:
                raise ValidationError(
                    "Le mot de passe ne correspond pas à sa validation"
                )

        # A réorganiser
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        existant_username = User.objects.get(username=username)
        print(existant_username)
        if existant_username is not None:
            print("reach")
            raise ValidationError(
                "Un compte possède déjà ce nom d'utilisateur."
            )

        existant_email = User.objects.get(email=email)
        if existant_email is not None:
            raise ValidationError("Un compte a déjà été créé avec cet email.")
