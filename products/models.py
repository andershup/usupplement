from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True) # can be null in the database and blank in forms

    def __str__(self):  
        return self.name 

    def get_friendly_name(self):
        return self.friendly_name #this one just returns the friendly name if we need


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) #set to null rather than deleting the product
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    first_sold = models.DateTimeField(auto_now_add=True, editable=True)
    uploaded_by = models.CharField(max_length=254, null=False, blank="True")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) #decimal field 
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name 


"""class SpecialDeals(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
   """  

