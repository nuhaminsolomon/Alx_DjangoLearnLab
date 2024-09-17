from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book  
from .serializers import BookSerializer
from rest_framework import viewsets  # Correct import for viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourModelSerializer
from .permissions import IsOwnerOrReadOnly
class YourModelViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission applied
class YourModelViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class AdminOnlyViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access
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
def book_list(request):
    books=Book.objects.all()
