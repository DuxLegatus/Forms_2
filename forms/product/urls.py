from django.contrib import admin
from django.urls import path,include
from .views import AddProductView,AllProductsView,SpecificProductView,UpdateProductView

urlpatterns = [
    path('add_product/', AddProductView.as_view(),name="add_product"),
    path("products/",AllProductsView.as_view(),name="all_products"),
    path("product/<int:pk>/",SpecificProductView.as_view(),name="product_detail"),
    path("update_product/<int:pk>/", UpdateProductView.as_view(),name="update_product")
]