from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list', views.products_list, name='products_list')
]