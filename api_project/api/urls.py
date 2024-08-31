
from django.urls import path
from .views import BookList  # Import the BookList view

# Define the URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map the 'books/' endpoint to the BookList view
]