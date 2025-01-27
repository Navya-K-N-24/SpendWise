from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('about/', views.about, name='about'),  # About page
    path('register/', views.register, name='register'), # URL for the registration page
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),  # Login page
    path('add/', views.add_transaction, name='add_transaction'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]