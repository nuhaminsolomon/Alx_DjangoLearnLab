
from django.urls import include, path
from .views import BookList  # Import the BookList view
from rest_framework.routers import DefaultRouter  # Import DefaultRouter from DRF
from .views import BookViewSet  # Import the BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Define the URL patterns using the router
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
# Define the URL patterns
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map the 'books/' endpoint to the BookList view
]