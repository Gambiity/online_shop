from django.urls import path
from. views import AboutView, TeamView, get_tab1_products, get_tab2_products, get_tab3_products, home_view

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
    path('Popular-Breakfast/', get_tab1_products, name='tab1'),
    path('Special-Lunch/', get_tab2_products, name='tab2'),
    path('Lovely-Dinner/', get_tab3_products , name='tab3'),
]