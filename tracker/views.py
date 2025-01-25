from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from django.http import HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.
# def home(request):
   # return HttpResponse("Welcome to SpendWise!")

def home(request):
    return render(request, "tracker/index.html")  

def about(request):
    return render(request, "tracker/about.html")

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

def login_view(request):
    # Login logic (assuming it exists)
    return render(request, 'tracker/login.html')

#def register(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       messages.success(request, 'Account created successfully! You can now log in.')
      #      return redirect('login')  # Replace 'login' with the URL name for the login page
    # else:
      #  form = UserCreationForm()
    # return render(request, 'tracker/register.html', {'form': form})