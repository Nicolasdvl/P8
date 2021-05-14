from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:id>/', views.substitutes, name='product_substitutes'),
    path('product/details/', views.details, name='product_details')
]