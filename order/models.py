from django.db import models
from user.models import UserModel
from product.models import ProductModel

class BookingModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    people = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.user.get_full_name
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductModel)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.get_full_name
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'