from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter
class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    

class BookListView(generics.ListAPIView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = 'books'  
    serializer_class = BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filter_fields = ['title','author','publication_year']
    search_fields = ['title','author']
    ordering_fields = ['title','author','publication_year']
    ordering = ['title']
class BookDetailView(DetailView):
    model = Book
   # template_name = 'book_detail.html'  
    context_object_name = 'book'  
class BookCreateView(CreateView):
    model = Book
   # template_name = 'book_form.html'  
    fields = ['title', 'author', 'published_date', 'isbn', 'summary'] 
    success_url = reverse_lazy('book-list')  


class BookUpdateView(UpdateView):
    model = Book
    #template_name = 'book_form.html'  
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']  
    success_url = reverse_lazy('book-list')  


class BookDeleteView(DeleteView):
    model = Book
   # template_name = 'book_confirm_delete.html'  
    context_object_name = 'book'
    success_url = reverse_lazy('book-list')  
    class BookCreateView(LoginRequiredMixin, CreateView):
     model = Book
    #template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model and perform additional actions.
        """
        
        form.instance.created_by = self.request.user  
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    #template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model and perform additional actions.
        """
        
        return super().form_valid(form)

    def test_func(self):
        """
        Ensure that only the user who created the book can update it.
        """
        book = self.get_object()
        return self.request.user == book.created_by