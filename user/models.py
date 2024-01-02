from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class UserModel(AbstractUser):
    phone = models.CharField(max_length=13)
    @property
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return 

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
