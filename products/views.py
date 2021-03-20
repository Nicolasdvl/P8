from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def results(request):
    results_list = Product.objects.all()
    context = {'results_list': results_list}
    return render(request, 'products/results.html', context)

def details(request):
    return HttpResponse("product details")