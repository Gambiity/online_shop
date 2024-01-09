from django.shortcuts import render, redirect
from django.views.generic import ListView ,TemplateView
from .models import TeamModel, BlogModel
from product.models import ProductModel
from user.models import CommentModel
from django.utils import timezone
from datetime import timedelta

week_ago = timezone.now() - timedelta(weeks=1)
comments = CommentModel.objects.filter(created_at__gte=week_ago)
blog = BlogModel.objects.all()
team = TeamModel.objects.all()


def get_tab1_products(request):
    if request.path == '/Popular-Breakfast/':
        products = ProductModel.objects.filter(category__name='tab1')
        return render(request, 'pages/index.html', context={
            'products': products,
            'objects': blog,
            'teammets': team,
            'comments': comments
        })
    
def get_tab2_products(request):
    if request.path == '/Special-Lunch/':
        products = ProductModel.objects.filter(category__name='tab2')
        return render(request, 'pages/index.html', context={
            'products':products,
            'objects':blog,
            'teammets': team,
            'comments': comments
        })
    
def get_tab3_products(request):
    if request.path == '/Lovely-Dinner/':
        products = ProductModel.objects.filter(category__name='tab3')
        return render(request, 'pages/index.html', context={
            'products':products,
            'objects':blog,
            'teammets': team,
            'comments': comments
        })

def home_view(request):
    return redirect('/Popular-Breakfast/')

class AboutView(ListView):
    model = TeamModel
    template_name = 'pages/about.html'
    context_object_name = 'teammets'

class TeamView(ListView):
    model = TeamModel
    template_name = 'pages/team.html'
    context_object_name = 'teammets'

