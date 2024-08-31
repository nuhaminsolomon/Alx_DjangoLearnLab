# api/serializers.py

from rest_framework import serializers  # Import Django REST framework serializers
from .models import Book  # Import the Book model from models.py

# Define the BookSerializer class
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model to be serialized
        fields = 'all'  # Include all fields from the Book model