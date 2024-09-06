from django.urls import path
from .views import AuthorListCreate, BookListCreate
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
   # path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/', BookListView.as_view(), name='book-list'),               
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   
    path('books/create', BookCreateView.as_view(), name='book-create'),        
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), 
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'), 


]
