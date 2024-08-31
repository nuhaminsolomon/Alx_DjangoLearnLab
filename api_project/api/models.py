from django.db import models

# Create your models here.
# api/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # A field to store the title of the book
    author = models.CharField(max_length=255)  # A field to store the author's name

    def str(self):
        return f"{self.title} by {self.author}"  # String representation of the Book model