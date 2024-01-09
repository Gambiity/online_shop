from django.db import models

class TeamModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.get_fullname
    
    class Meta:
        verbose_name = 'team'


class BlogModel(models.Model):
    text = models.TextField()
    years = models.PositiveIntegerField()
    masters = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

