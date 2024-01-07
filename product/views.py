from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import ProductModel, CategoryModel


def get_tab1_products(request):
    if request.path == '/product/Popular-Breakfast/':
        products = ProductModel.objects.filter(category__name='tab1')
        return render(request, 'pages/menu.html', context={
            'products':products
        })
    
def get_tab2_products(request):
    if request.path == '/product/Special-Lunch/':
        products = ProductModel.objects.filter(category__name='tab2')
        return render(request, 'pages/menu.html', context={
            'products':products
        })
    
def get_tab3_products(request):
    if request.path == '/product/Lovely-Dinner/':
        products = ProductModel.objects.filter(category__name='tab3')
        return render(request, 'pages/menu.html', context={
            'products':products
        })