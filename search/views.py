from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from products.models import Product


def index(request):
    return render(request, 'search/index.html')

def products_list(request):
    results_list = Product.objects.all()
    names = [(product.name, product.id) for product in results_list]
    return JsonResponse(names, safe=False)