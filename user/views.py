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
            messages.success(request, 'Successfully signed in')
            return redirect('/order/booking/') 
        else:
            messages.error(request, 'There was an error logging in. Please try again.')
            return redirect('/user/contact/')
    return render(request, 'pages/login.html')

def contact_view(requset):
    if requset.method == 'POST':
        first_name = requset.POST['first_name']
        last_name = requset.POST['last_name']
        email = requset.POST['email']
        phone = requset.POST['phone']
        password = requset.POST['password']
        username = requset.POST['username']
        user = UserModel(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password, username=username)
        user.save()
        return redirect('/user/login/')
    return render(requset,'pages/contact.html')

def logout(request):
    auth_logout(request)
    return redirect('/user/contact/')