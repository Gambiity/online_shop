from typing import Any, Dict
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from .models import UserModel, CommentModel
from django.contrib import messages

class UserView(CreateView):
    model = UserModel
    template_name = 'pages/contact.html'
    success_url = '/'
    fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password']

    
class LoginView(LoginView):
    template_name = 'layouts/footer.html'
    success_url = '/'

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Invalid credentials')
        print('otmadi')
        return super().form_invalid(form)
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        print('otti')
        return super().form_valid(form)
    
class LogOutView(LogoutView):
    next_page = '/'