from django.urls import path

from . import views

urlpatterns = [
    path('product/id/', views.substitutes, name='product_substitutes'),
]