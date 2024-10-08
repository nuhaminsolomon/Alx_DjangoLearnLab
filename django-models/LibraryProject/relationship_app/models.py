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

    