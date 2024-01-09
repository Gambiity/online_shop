from django.urls import path
from .views import contact_view, login, logout, TestimonialView

app_name = 'user'

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
]