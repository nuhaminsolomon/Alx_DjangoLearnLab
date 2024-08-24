from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})

# Create your views here.
