from django.shortcuts import render, get_object_or_404

from .models import Product, Category, Sort

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

    sort_option = request.GET.get('sort')
    sort_mapping = {
        "price: lowest first": "price",
        "price: highest first": "-price",
        "date: newest first": "create_date",
        "date: oldest first": "-create_date",
    }
    sort_by = sort_mapping.get(sort_option, "create_date")

    products = Product.objects.filter(**filters).order_by(sort_by)
    categories = Category.objects.all()
    sorts = Sort.objects.filter().order_by()




    return render(request, 'home.html', {'products': products, 'categories': categories, 'sorts': sorts})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    product.views += 1
    product.save()
    return render(request, 'product_detail.html', {"product": product})

