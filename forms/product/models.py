from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    in_stock = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_desc = models.TextField()
    
    def __str__(self):
        return self.product_name
    

class ProductLog(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='logs')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'log for {self.product.name} : {self.message[:30]}'
