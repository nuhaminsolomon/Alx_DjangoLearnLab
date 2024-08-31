from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book  
from .serializers import BookSerializer
from rest_framework import viewsets  # Correct import for viewsets

# Define the BookViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    A Viewsets that provides the standard actions for the Book model.
    """
    queryset = Book.objects.all()  # Define the queryset to retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization    


class BookList( generics.ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer

