from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db import IntegrityError

from .forms import CustomUserCreationForm, CustomUserLoginForm, TransactionForm
from .models import Transaction


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
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Update 'login' if the URL name differs
    else:
        form = CustomUserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

# Admin dashboard view
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    return render(request, 'tracker/admin_dashboard.html')

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user role
                if user.role == 'admin':
                    return redirect('admin_dashboard')  # If admin, go to admin dashboard (you can adjust the URL)
                else:
                    return redirect('dashboard')  # Redirect to a dashboard view
    else:
        form = CustomUserLoginForm()
    return render(request, 'tracker/login.html', {'form': form})

@login_required
def dashboard(request):
    # Fetch the logged-in user's transactions
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

# All Transaction view
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})


# Add Transaction view

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)  # Don't save to the database yet
            transaction.user = request.user       # Assign the logged-in user
            try:
                transaction.save()                # Save to the database
                messages.success(request, "Transaction added successfully!")
                return redirect('transaction_list')  # Redirect to the transaction list page
            except IntegrityError:
                messages.error(request, "Failed to add transaction. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transaction.html', {'form': form})

# Edit transaction
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if transaction.user != request.user:
        messages.error(request, "You do not have permission to edit this transaction.")
        return redirect('transaction_list')  # Or redirect to the dashboard

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'tracker/edit_transaction.html', {'form': form,'transaction': transaction})

# Delete Transaction
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

     # Ensure the transaction belongs to the logged-in user
    if transaction.user != request.user:
        messages.error(request, "You do not have permission to delete this transaction.")
        return redirect('transaction_list')  # Or redirect to the dashboard
    
    if request.method == 'POST':  
        transaction.delete()
        return redirect('transaction_list')  
    
    return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout