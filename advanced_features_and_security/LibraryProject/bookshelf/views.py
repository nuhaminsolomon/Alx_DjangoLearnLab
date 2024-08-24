from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
User = get_user_model()
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    # Your view logic here
    return render(request, 'edit_template.html')


# views.py

from django.shortcuts import render
from .forms import ExampleForm

def book_list(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()
    books = Book.objects.all()
    return render(request, 'bookshelf/form.html', {'form': form, 'books': books})
