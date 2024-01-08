from django.urls import path
from. views import HomeView, AboutView, TeamView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
]