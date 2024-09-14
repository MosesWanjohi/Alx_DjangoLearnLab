from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.URLField(blank=True)
    def __str__(self):
        return self.title
    