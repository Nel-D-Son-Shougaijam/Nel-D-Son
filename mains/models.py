from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Story(models.Model):
    thumb = models.ImageField(upload_to='media/', default='static/blog_cover.jpg',blank=True)
    name = models.CharField(max_length=120,default=models.DateField(auto_now_add=True))
    slug = models.SlugField(default=models.AutoField())
    maint = models.TextField()
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_articles')
    def number_of_likes(self):
       return self.likes.count()
    def sl(self):
        return self.maint[0:15]
