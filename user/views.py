from typing import Any, Dict
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserModel, CommentModel
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully signed in')
            return redirect('/')  #booking
        else:
            messages.error(request, 'There was an error logging in. Please try again.')
            return redirect('/user/contact/')
    return render(request, 'pages/login.html')

class UserView(CreateView):
    model = UserModel
    template_name = 'pages/contact.html'
    success_url = '/user/login/'
    fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password']



def logout(request):
    auth_logout(request)
    return redirect('/user/contact/')