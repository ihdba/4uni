from django.shortcuts import render

# Create your views here.

from .models import Product

def eshop(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'eshop/home.html', context)