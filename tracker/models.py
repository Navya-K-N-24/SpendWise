from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('transport', 'Transport'),
        ('others', 'Others'),
    ]

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f'{self.category} - {self.amount} on {self.date}'
