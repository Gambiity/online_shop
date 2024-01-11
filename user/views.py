from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserModel, CommentModel
from django.contrib import messages

class TestimonialView(ListView):
    model = CommentModel
    template_name = 'pages/testimonial.html'
    context_object_name = 'objects'

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/order/booking/') 
        else:
            error = 'Username or Password uncorrect!'
            return render(request, 'pages/login.html', context={
                'error': error
            })
    return render(request, 'pages/login.html')

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        username = request.POST['username']
        confirm_password = request.POST['confirm_password']
        img = request.FILES['img']
        if password != confirm_password:
            error = 'Passwords are not the same'
            return render(request, 'pages/contact.html', context={
                'error':error
            })
        user = UserModel(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password, username=username, img=img)
        user.save()
        return redirect('/user/login/')
    return render(request,'pages/contact.html')

def logout(request):
    auth_logout(request)
    return redirect('/user/contact/')