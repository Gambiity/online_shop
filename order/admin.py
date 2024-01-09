from django.contrib import admin
from .models import BookingModel

@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
