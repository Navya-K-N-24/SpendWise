from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Custom User model for role-based authentication
class CustomUser(AbstractUser):
    # You can add additional fields for roles or other customizations here
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name=_("Role")
    )

    def __str__(self):
        return self.username


# Transaction model for tracking expenses
class Transaction(models.Model):
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('groceries', 'Groceries'),
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(
        CustomUser,  # Ensure this references the custom user model
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    date = models.DateField(verbose_name=_("Transaction Date"))
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Amount")
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name=_("Category")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        ordering = ['-date']
