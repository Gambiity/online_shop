from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import TeamModel

class HomeView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(ListView):
    model = TeamModel
    template_name = 'pages/about.html'
    context_object_name = 'teammets'

class TeamView(ListView):
    model = TeamModel
    template_name = 'pages/team.html'
    context_object_name = 'teammets'