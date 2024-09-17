
from django.urls import include, path
from .views import BookList, BookViewSet  # Import the BookList view
from rest_framework.routers import DefaultRouter  # Import DefaultRouter from DRF
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken

urlpatterns = [
    # Other URL patterns...
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
]
urlpatterns = [
    # Other URL patterns...
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
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