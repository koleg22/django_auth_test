
# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'main/home.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Редирект на страницу входа
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})