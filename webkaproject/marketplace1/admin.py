from django.contrib import admin
from .models import Product
from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'is_active', 'published_date']
    list_filter = ['is_active', 'published_date']
    list_editable = ['cost', 'is_active']
admin.site.register(Product, ProductAdmin)
