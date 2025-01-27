from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .forms import TransactionForm
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
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Update 'login' if the URL name differs
    else:
        form = CustomUserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a dashboard view
    else:
        form = CustomUserLoginForm()
    return render(request, 'tracker/login.html', {'form': form})

# Add Transaction view
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction added successfully!")
            return redirect('transaction_list')  # Redirect to the transaction list page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transaction.html', {'form': form})

# All Transaction view
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

# Edit transaction
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'tracker/edit_transaction.html', {'form': form, 'transaction': transaction})

# Delete Transaction
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    
    if request.method == 'POST':  
        transaction.delete()
        return redirect('transaction_list')  
    
    return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})