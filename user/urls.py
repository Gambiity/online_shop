from django.urls import path
from .views import UserView, LoginView, LogOutView

app_name = 'user'

urlpatterns = [
    path('contact/', UserView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
]