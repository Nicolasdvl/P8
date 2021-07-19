"""
Django form for authentification app.

Python class to build a form.
"""
from django import forms


class SearchForm(forms.Form):
    """Declaration of form fields to build a search bar."""

    product_id = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "product_id"})
    )
    myInput = forms.CharField(
        label="", widget=forms.TextInput(attrs={"id": "myInput"})
    )
