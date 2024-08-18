from django.db import models


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=100)
    author= models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name='libraries')
    def __str__(self):
        return self.name
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library,related_name='librarian',on_delete=models.CASCADE)
    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import   
 receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES   
 = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


from django.db import models
from django.contrib.auth.models import PermissionsMixin

class Book(models.Model, PermissionsMixin):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

    def __str__(self):
        return self.title
