from django.contrib import admin
from .models import UserModel, CommentModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'id']
    list_display_links = ['first_name', 'last_name', 'id']

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']
    list_display_links = ['user', 'id']