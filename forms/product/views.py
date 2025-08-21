from django.shortcuts import render,redirect,get_object_or_404
from .forms import Product_form
from .models import Products
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponseNotAllowed
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixins import QueryParamsMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

class AllProductsView(QueryParamsMixin,ListView):
    model = Products
    template_name = "product/all_products.html"
    context_object_name = "products"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if query:
            queryset = queryset.filter(Q(product_name__icontains=query))

        if category:
            queryset = queryset.filter(category__name=category)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        order_by = self.request.GET.get('order_by')  
        if order_by in ['product_name', '-product_name', 'price', '-price', 'id', '-id']:
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by('id')
        return queryset
    

class SpecificProductView(DetailView):
    model = Products
    template_name = "product/product_detail.html"
    context_object_name = "product"


class AddProductView(LoginRequiredMixin,CreateView):
    model = Products
    form_class = Product_form
    template_name = "product/add_product.html"
    success_url = reverse_lazy('all_products')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        
class UpdateProductView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Products
    form_class = Product_form
    template_name = "product/update_product.html"
    success_url = reverse_lazy('all_products')
    def post(self, request, *args, **kwargs):
        method = request.POST.get('_method', '').upper()
        if method != 'PUT':
            return HttpResponseNotAllowed(['PUT'])
        return super().post(request, *args, **kwargs)
    
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden('only owner can change the product')
        return super().handle_no_permission()

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs = {'pk': self.object.pk} )
