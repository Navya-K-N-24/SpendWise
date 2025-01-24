from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to SpendWise!")

def register(request):
    return render(request, 'tracker/register.html')