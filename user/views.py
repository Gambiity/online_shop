from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django import forms
from .models import UserModel, CommentModel

class UserView(CreateView):
    model = UserModel
    template_name = 'pages/contact.html'
    success_url = '/'
    fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    
