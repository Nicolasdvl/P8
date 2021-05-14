from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def substitutes(request, id):  
    product = Product.objects.get(id=id)
    substitutes_list = get_subs_list(product)
    context = {
    'product': product,
    'substitute1': substitutes_list[0],
    'substitute2': substitutes_list[1],
    'substitute3': substitutes_list[2],
    'substitute4': substitutes_list[3],
    'substitute5': substitutes_list[4],
    'substitute6': substitutes_list[5]
    }
    return render(request, 'products/substitutes.html', context)

def details(request):
    return render(request, 'products/details.html')

def get_subs_list(product):
    categories = product.categories.all()
    products_list = []
    for category_name in categories:
        category = Category.objects.get(name=category_name)
        relevant_products_list = category.product_set.all()
        for relevant_product in relevant_products_list:
            products_list.append(relevant_product)
    while product in products_list:
        products_list.remove(product)
    substitutes_list = []
    for element in products_list:
        count = products_list.count(element)
        if (count, element) not in substitutes_list:
            substitutes_list.append((count, element))
    substitutes_list.sort(key=index, reverse=True)
    substitutes_list_sorted=[]
    for substitute in substitutes_list[0:6]:
        substitutes_list_sorted.append(substitute[1])
    return substitutes_list_sorted

def index(element):
    return element[0]