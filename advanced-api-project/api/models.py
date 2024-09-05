from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)  # String field for the author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # String field for the book's title
    publication_year = models.IntegerField()  # Integer field for the publication year
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Foreign key to Author model

    def __str__(self):
        return self.title

