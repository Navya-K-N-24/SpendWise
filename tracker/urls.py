from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('register/', views.register, name='register'), # URL for the registration page
]
