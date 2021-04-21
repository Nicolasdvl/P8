from django.shortcuts import render
from products.models import Product

# Create your views here.

def substitutes(request):
    r = request.POST
    print(r)
    product = Product.objects.get(name=r['product_search'])
    subs = {'prod': {'name': product.name}}
    return render(request, 'products/substitutes.html', subs)

def details(request):
    return HttpResponse("product details")