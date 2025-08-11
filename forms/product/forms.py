from django import forms
from .models import Products

class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["product_name","price","in_stock","product_desc"]

