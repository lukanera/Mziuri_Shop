from django.contrib import admin
from .models import Product, Category, Sort

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sort)