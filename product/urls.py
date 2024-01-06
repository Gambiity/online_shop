from django.urls import path
from .views import ProductView

app_name = 'product'

urlpatterns = [
    path('Popular-Breakfast/', ProductView.as_view(), name='tab1'),
    path('Special-Lunch/', ProductView.as_view(), name='tab2'),
    path('Lovely-Dinner/', ProductView.as_view(), name='tab3'),
]