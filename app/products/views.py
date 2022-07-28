"""
Django views for products app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentification.models import User
from products.models import Product
from search.search import SearchForm

# Create your views here.


def substitutes(request, id):
    """Return a html page with a list of products and a form."""
    product = Product.objects.get(id=id)
    search_form = SearchForm()
    context = {
        "product": product,
        "substitutes": product.get_subs_list(),
        "SearchForm": search_form,
    }
    if "submit_save" in request.POST:
        submit = request.POST.get("submit_save")
        submit = submit.split()
        product = Product.objects.get(id=submit[0])
        user = User.objects.get(id=submit[1])
        product.users_saves.add(user)
        product.save()
    return render(request, "products/substitutes.html", context)


def details(request, id):
    """Return a html page with details of a product selected."""
    product = Product.objects.get(id=id)
    search_form = SearchForm()
    context = {"product": product, "SearchForm": search_form}
    return render(request, "products/details.html", context)


@login_required
def my_substitutes(request):
    """Return a html page with a list of products saved by user."""
    user = request.user
    search_form = SearchForm()
    context = {"products": user.get_saves(), "SearchForm": search_form}
    return render(request, "products/saves.html", context)
