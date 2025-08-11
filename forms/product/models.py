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
