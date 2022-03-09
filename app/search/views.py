"""
Django views for search app.

Python functions that takes a Web request and returns a Web response.
This response can be the HTML contents of a Web page, or a redirect,
or a 404 error, or an XML document, or an image . . .
"""

from django.http import JsonResponse
from products.models import Product


def products_list(request):
    """Return a json with name and id of all products."""
    results_list = Product.objects.all()
    names = [(product.name, product.id) for product in results_list]
    return JsonResponse(names, safe=False)
