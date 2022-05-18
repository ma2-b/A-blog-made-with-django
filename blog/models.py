from django.db import models 
from django.contrib.auth.models import User
from django.urls import reverse   
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver


# create your views here 

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=277)
    #body = models.TextField() 
    body = RichTextField(blank=True,null=True)
    img = models.ImageField(blank=True,null=True,upload_to='images/')
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='likes')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
     
    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[str(self.id)]) 
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:posts') 
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField() 
    profile_pic = models.ImageField(upload_to="profile_pic",null=True,blank=True)
    webiste_url = models.CharField(max_length=70,null=True,blank=True)
    facebook_url = models.CharField(max_length=70,null=True,blank=True)
    instagram_url = models.CharField(max_length=70,null=True,blank=True)
    


    def __str__(self):
        return str(self.user)



    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

    
    
    
