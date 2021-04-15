from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/id/', views.results, name='products_details'),
]