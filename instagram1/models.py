from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank= True, null=True)
    imageName = models.TextField()
    image_caption = models.TextField()
    profile = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.image_caption
    
    class Meta:
        ordering = ['created_date']
        
class Profile(models.Model):
    profilePhoto= models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User, related_name='Profile', null=True, on_delete=models.CASCADE,blank=True,)
    name = models.CharField(blank=True, max_length=150)
    # post = HTMLField()
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_user(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles
    
    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
    

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, related_name='Comments', null=True, on_delete=models.CASCADE,blank=True,)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Image'

    class Meta:
        ordering = ["-pk"]