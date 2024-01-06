from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import ProductModel, CategoryModel

class ProductView(ListView):
    model = ProductModel
    template_name = 'pages/menu.html'
    context_object_name = 'products'

