from django.db import models
# Necessary imports
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    
    # Need to be done
    
    slug = models.SlugField(max_length=200, unique=True)
    product_description = models.TextField(max_length=500, default="")
    price = models.IntegerField()
    image = models.ImageField(upload_to="./photos/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True);
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now = True)
     
    
    # Get the url
    def get_url(self):
        return reverse('product-detail', args=[self.category.slug, self.slug])
    
    # String Representation 
    def __str__(self):
        return self.product_name