from django.urls import path
from .views import booking_view
app_name = 'order'

urlpatterns = [
    path('booking/', booking_view, name='booking'),
]