from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentification.forms.signup import SingupForm
from authentification.forms.login import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages


def signup(request):
    """Send a signup form and redirect to index.html when form is valid."""
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
            )
            user.save()
            return redirect("index")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Le nom d'utilisateur et/ou l'email est/sont déjà utilisé/s",
            )
            login_form = SingupForm()
            context = {"SignUpForm": login_form, "message": messages}
            return render(request, "authentification/signup.html", context)
    else:
        signup_form = SingupForm()
        context = {"SignupForm": signup_form}
        return render(request, "authentification/signup.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Les informations de connections sont invalides.",
                )
    login_form = LoginForm()
    context = {"LoginForm": login_form}
    return render(request, "authentification/login.html", context)


def logout_user(request):
    logout(request)
    return render(request, "core/index.html")
