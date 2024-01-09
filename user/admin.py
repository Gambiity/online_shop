from django.contrib import admin
from .models import UserModel, CommentModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_display_links = ['id', 'first_name', 'last_name']

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']