"""
Django views for authentification app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render, redirect
from authentification.forms.signup import SignupForm
from authentification.forms.login import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


def signup(request):
    """Send a signup form and redirect to index.html when form is valid."""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(make_password(form.cleaned_data["password"]))
            user.save()

            return redirect("index")
    else:
        form = SignupForm()
    context = {"SignupForm": form}
    return render(request, "authentification/signup.html", context)


def login_user(request):
    """Send a login form and redirect to index.html when form is valid."""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("REACH===========================")
            email = request.POST["email"]
            password = request.POST["password"]
            print(password)

            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                print("REACH login==================")
                login(request, user)
                return redirect("index")
    else:
        form = LoginForm()
    context = {"LoginForm": form}
    return render(request, "authentification/login.html", context)


def logout_user(request):
    """Call the logout function and redirect to the index page."""
    logout(request)
    return redirect("index")
