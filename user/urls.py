from django.urls import path
from .views import UserView, login, logout

app_name = 'user'

urlpatterns = [
    path('contact/', UserView.as_view(), name='contact'),
    path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
]