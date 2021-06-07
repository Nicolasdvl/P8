from django.shortcuts import render
from products.models import Product, Category
from search.search import SearchForm

# Create your views here.


def substitutes(request, id):
    product = Product.objects.get(id=id)
    form = SearchForm()
    context = {
        "product": product,
        "substitutes": product.get_subs_list(),
        "form": form,
    }
    return render(request, "products/substitutes.html", context)


def details(request):
    return render(request, "products/details.html")
