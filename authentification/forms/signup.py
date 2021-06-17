from django import forms


class SingupForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"id": "username"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={"id": "email"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"id": "password"}),
    )
    confirme = forms.CharField(
        label="Confirme your password",
        widget=forms.PasswordInput(attrs={"id": "confirme"}),
    )
