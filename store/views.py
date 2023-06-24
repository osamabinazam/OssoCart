from django.shortcuts import render
from .models import Product
# Create your views here.

# Rendering Store that list all available Products

def Store(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products,
    }
    return render(request, 'ossocart/store.html', context)
