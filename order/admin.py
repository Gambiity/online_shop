from django.contrib import admin
from .models import BookingModel, OrderModel

@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']