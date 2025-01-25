from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# Home page view
def home(request):
    return render(request, "tracker/index.html")

# About page view
def about(request):
    return render(request, "tracker/about.html")

# User registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Update 'login' if the URL name differs
    else:
        form = CustomUserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})
