# api/urls.py

from django.urls import path
from .views import AuthorListCreate, BookListCreate

urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
]
