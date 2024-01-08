from django.shortcuts import render
from .models import ProductModel


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