from django.db import models

# Create your models here.

# Category Model that Reflect a table in Database
class Category(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.CharField(max_length=100, unique=True)            # Store url of category
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='./photos/categories')
    
    
    # String Representation of Model
    def __str__(self):
        return self.category_name

    # 
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
            
    
