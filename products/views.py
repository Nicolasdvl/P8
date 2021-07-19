"""
Django views for products app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""
from django.shortcuts import render
from products.models import Product
from search.search import SearchForm

# Create your views here.


def substitutes(request, id):
    """Return a html page with a list of products and a form."""
    product = Product.objects.get(id=id)
    form = SearchForm()
    context = {
        "product": product,
        "substitutes": product.get_subs_list(),
        "form": form,
    }
    return render(request, "products/substitutes.html", context)


def details(request):
    """Return a html page."""
    return render(request, "products/details.html")
