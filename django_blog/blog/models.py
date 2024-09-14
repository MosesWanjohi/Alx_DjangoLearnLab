from django.db import models
from django.contrib.auth.models import User

# Create your models here.
user = User.objects.create_user(username='username', password='password', email='email', first_name='first_name', last_name='last_name')
user.save()
class Create_User(User):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    