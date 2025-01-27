from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
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
