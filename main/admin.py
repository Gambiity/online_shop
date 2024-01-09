from django.contrib import admin
from .models import TeamModel, BlogModel

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_fullname']
    list_display_links = ['id', 'get_fullname']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
