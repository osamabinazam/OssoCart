from django.contrib import admin
from .models import Product
# need to be done 

# Prepopulate the model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock', 'category', 'modify_date' )
    prepopulated_fields = {'slug' : ('product_name',)}

# Register Product Model
admin.site.register(Product, ProductAdmin)

