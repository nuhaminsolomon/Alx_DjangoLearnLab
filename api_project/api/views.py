from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView  # Import ListAPIView from Django REST framework
from .models import Book  # Import the Book model from models.py
from .serializers import BookSerializer  # Import the BookSerializer from serializers.py

# Define the BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Set the queryset to include all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data