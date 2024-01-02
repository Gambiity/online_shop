from django.contrib import admin
from .models import ContactModel, TeamModel, BlogModel

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['get_fullname']
    list_display_links = ['get_fullname']

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name', 'created_at']

@admin.register(BlogModel)
class BloGAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
