from django.db import models

# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_desc = models.TextField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.product_name

class Order(models.Model):
     
     items = models.CharField(max_length=1000)
     name = models.CharField(max_length=500)
     city = models.CharField(max_length=500)
     state = models.CharField(max_length=500)
     address = models.CharField(max_length=1000)
     zip = models.CharField(max_length=500)
     email = models.CharField(max_length=500)
     
     
     
     
     def __str__(self):
         return self.name
     