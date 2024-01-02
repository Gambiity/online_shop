from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    product_img = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
