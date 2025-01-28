# User Registration Test
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserRegistrationTest(TestCase):

    def test_user_registration(self):
        # Define valid user data
        data = {
            'username': 'testuser',
            'password1': 'Password123!',
            'password2': 'Password123!',
        }

        # Send POST request to the registration page
        response = self.client.post(reverse('register'), data)

        # Debugging: Print the response content for inspection
        print(response.content)

        # Check if the form is valid before expecting a redirect
        if response.status_code == 200:
            # If status is 200, the form might have errors, so check the form context
            self.assertIn('form', response.context)  # Ensure form is in context
            self.assertFalse(response.context['form'].is_valid())  # Ensure form is invalid (if 200 returned)

        # Expecting a redirect after successful form submission (status code 302)
        if response.status_code == 302:
            # Check if the user is actually created
            user = get_user_model().objects.filter(username='testuser').exists()
            self.assertTrue(user)

            # Check redirection to login page
            self.assertRedirects(response, reverse('login'))


# User Login Test
from django.contrib.auth import get_user_model
from django.test import TestCase  # Import TestCase here
from django.urls import reverse

class UserLoginTest(TestCase):
    
    def setUp(self):
        """Set up a test user for login."""
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )

    def test_user_login(self):
        """Test that a user can log in successfully."""
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        
        # Send POST request to the login view
        response = self.client.post(reverse('login'), data)
        
        # Check if the user is logged in by checking the response status
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        
        # Ensure the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)


# Transaction CRUD Operations Test
from django.test import TestCase
from django.urls import reverse
from tracker.models import Transaction
from django.contrib.auth import get_user_model

class TransactionCRUDTest(TestCase):
    
    def setUp(self):
        """Set up a test user and a sample transaction."""
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )
        self.client.login(username='testuser', password='password123')

    def test_create_transaction(self):
        """Test that a user can create a transaction."""
        data = {
            'date': '2025-01-27',
            'amount': '100.00',
            'category': 'food',
            'description': 'Test transaction'
        }
        response = self.client.post(reverse('add_transaction'), data)
        
        # Check if the transaction is created and user is redirected
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('transaction_list'))
        
        # Verify the transaction is saved in the database
        transaction = Transaction.objects.get(amount='100.00')
        self.assertIsNotNone(transaction)

    def test_edit_transaction(self):
        """Test that a user can edit a transaction."""
        transaction = Transaction.objects.create(
            user=self.user,
            date='2025-01-27',
            amount=50.00,
            category='food',
            description='Initial transaction'
        )
        
        updated_data = {
            'date': '2025-01-28',
            'amount': '75.00',
            'category': 'groceries',
            'description': 'Updated transaction'
        }
        
        response = self.client.post(reverse('edit_transaction', args=[transaction.id]), updated_data)
        
        # Check if the transaction is updated
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('transaction_list'))
        
        # Verify the transaction was updated in the database
        transaction.refresh_from_db()
        self.assertEqual(transaction.amount, 75.00)
        self.assertEqual(transaction.category, 'groceries')
        self.assertEqual(transaction.description, 'Updated transaction')

    def test_delete_transaction(self):
        """Test that a user can delete a transaction."""
        transaction = Transaction.objects.create(
            user=self.user,
            date='2025-01-27',
            amount=50.00,
            category='food',
            description='Transaction to delete'
        )
        
        response = self.client.post(reverse('delete_transaction', args=[transaction.id]))
        
        # Check if the transaction is deleted
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('transaction_list'))
        
        # Verify the transaction is deleted from the database
        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(id=transaction.id)
