from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def substitutes(request, id):  
    product = Product.objects.get(id=id)
    context = {
    'product': product,
    'substitutes': product.get_subs_list()
    }
    print(context['substitutes'])
    return render(request, 'products/substitutes.html', context)

def details(request):
    return render(request, 'products/details.html')
