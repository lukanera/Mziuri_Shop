from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product, Category

def home(request):
    filters = dict()

    product_name = request.GET.get('product_name')
    if product_name:
        filters['name__icontains'] = product_name

    min_price = request.GET.get('min_price')
    if min_price:
        filters['price__gte'] = min_price

    max_price = request.GET.get('max_price')
    if max_price:
        filters['price__lte'] = max_price

    address = request.GET.get('address')
    if address:
        filters['address__icontains'] = address

    category = request.GET.get('category')
    if category:
        filters['category_id']  = category

    sort_by = request.GET.get('sort')

    products = Product.objects.filter(**filters)
    if sort_by:
        products = products.order_by(sort_by)
    categories = Category.objects.all()



    return render(request, 'home.html', {'products': products, 'categories': categories})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    product.views += 1
    product.save()
    return render(request, 'product_detail.html', {"product": product})

def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your product has been created successfully.')
            return redirect('home')
    return render(request, 'product_form.html', {'form': form})

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your product has been updated successfully.')
            return redirect('home')
    return render(request, 'update_product.html', {'form': ProductForm(instance=product)})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, f'{product.name} has been deleted successfully.')
    return redirect('home')

