from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('transport', 'Transport'),
        ('others', 'Others'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    

    def __str__(self):
        return f'{self.category} - {self.amount} on {self.date}'

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username
