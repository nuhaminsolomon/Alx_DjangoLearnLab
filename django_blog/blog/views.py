from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

