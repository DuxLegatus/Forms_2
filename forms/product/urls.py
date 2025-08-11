from django.contrib import admin
from django.urls import path,include
from .views import add_product,show_products,show_specific_products,update_product

urlpatterns = [
    path('add_product/', add_product,name="add_product"),
    path("products/",show_products,name="all_products"),
    path("product/<int:pk>/",show_specific_products,name="product_detail"),
    path("update_product/<int:pk>/", update_product,name="update_product")
]