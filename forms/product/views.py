from django.shortcuts import render,redirect,get_object_or_404
from .forms import Product_form
from .models import Products
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponseNotAllowed

# Create your views here.

def show_products(request):
    products = Products.objects.all()
    return render(request,"product/all_products.html",{"products":products})

def show_specific_products(request,pk):
    product = get_object_or_404(Products,pk=pk)
    return render(request,"product/product_detail.html",{"product":product})



@login_required
def add_product(request):
    if request.method == "POST":
        form = Product_form(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("all_products")
    else:
        form = Product_form()
    return render(request, 'product/add_product.html', {'form': form})

@login_required
def update_product(request,pk):
    product = get_object_or_404(Products,pk=pk)
    if not request.user == product.user:
        return HttpResponseForbidden("you havent uploaded this product")
    if request.method == "POST":
        method = request.POST.get("_method","").upper()
        if method == "PUT":
            form = Product_form(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('all_products')
        else:
            return HttpResponseNotAllowed(["PUT"])
    else:
        form = Product_form(instance=product)

    return render(request, 'product/update_product.html', {'form': form,"product":product})

        
