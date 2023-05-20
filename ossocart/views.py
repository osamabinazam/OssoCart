from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    context = {}
    return render(request, 'ossocart/home.html', context)