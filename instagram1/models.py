from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_picture = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(max_length=500, default="", blank=True)
    name = models.CharField(blank=True, max_length=20)
    location = models.CharField(max_length=60, blank=True)

    
    def __str__(self):
		   return self.name
    
    
    def delete_profile(self):
		   self.delete()



    def save_profile(self):
		   self.save()

    @classmethod
    def search_profile(cls,search_term):
		   got_profiles = cls.objects.filter(name__icontains = search_term)
		   return got_profiles



class Image(models.Model):
    image = models.ImageField(upload_to='images/',null = True)
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    # comments = models.ForeignKey(default="")

    def __str__(self):
    	return self.name
 
    def update_caption(self,new_caption):
    	self.caption = new_caption
    	self.save()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_images_by_id(cls,id):
        fetched_image = Image.objects.get(id = id)
        return  fetched_image

    @classmethod
    def get_images_by_user(cls,id):
        sent_images = Image.objects.filter(user_id=id)
        return sent_images

    def total_likes(self):
        return self.likes.count()
    
    class Meta:
    	ordering = ['-created']
 
    
    def save_profile(self):
    	self.save()
    


class Comment(models.Model):
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
           return self.comment
    def delete_comment(self):
		   self.delete()
    def save_comment(self):
		   self.save()
        
        
class Follow(models.Model):
	user = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
	follower = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
	user = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
	follower = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

	def __int__(self):
		return self.name

class Likes(models.Model):
	user = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 





