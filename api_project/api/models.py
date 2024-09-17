from django.db import models
from api.views import YourView
from api.models import YourModel


class Book(models.Model):
    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=255)  

    def str(self):
        return f"{self.title} by {self.author}"  