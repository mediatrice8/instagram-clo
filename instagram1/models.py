from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank= True, null=True)
    imageName = models.TextField()
    image_caption = models.TextField()
    profile = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
