from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    product.views += 1
    product.save()
    return render(request, 'product_detail.html', {"product": product})

