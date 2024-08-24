from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    

#Custom User Model by extending AbstractUser
#from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        #Validating Email
        if not email:
            raise ValueError('User must have an email address')
        #Fetching and normalizing email
        user=self.model(email=self.normalize_email(email)),

        #Setting password (hashes password)
        user.set_password(password)
        #saving created user in current database
        user.save(self._db)
        #returning created user
        return user
    
    #creating superuser ensuring administrative users can be created with the required fields fields
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user
      
