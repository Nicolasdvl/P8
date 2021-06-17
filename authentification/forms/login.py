from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-mail", widget=forms.TextInput(attrs={"id": "email"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"id": "password"})
    )
