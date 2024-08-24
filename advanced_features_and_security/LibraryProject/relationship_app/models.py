from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

#Extending Book Model with Custom Permissions
    class Meta:
        permissions =(
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),

        )

    def __str__(self):
        return f"{self.title} by {self.author}"  

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name   

    def get_books_list(self):
        return ", ".join([book.title for book in self.books.all()])


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
    
#Extending User Model with a UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    ROLE_CHOICES =(
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    
    )

    role = models.CharField(max_length=50,  choices=ROLE_CHOICES, default='Member')
    userprofile = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.role}'

#Signal to automatically create a UserProfile when a new User is created
#from django.db.models.signals import post_save
#from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    