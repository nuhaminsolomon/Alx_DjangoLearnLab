from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
def list_books(request):
  books=Book.objects.all()
  return render(request,'relationship_app/list_books.html',{'books':books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your desired homepage
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'relationship_app/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect back to login page

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.userprofile.role == 'admin'

def user_is_librarian(user):
    return user.userprofile.role == 'librarian'

def user_is_member(user):
    return user.userprofile.role == 'member'

@user_passes_test(user_is_admin)
def admin_view(request):
    # Admin-specific content here
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    # Librarian-specific content here
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    # Member-specific content here
    return render(request, 'relationship_app/member_view.html')
