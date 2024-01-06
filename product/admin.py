from django.contrib import admin
from .models import ProductModel, CategoryModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
