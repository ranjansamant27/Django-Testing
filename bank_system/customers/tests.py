from django.test import TestCase
from .models import Customer
# unit testing. individual test methods we have for functions in customer model.
class CustomerModelTest(TestCase):
    def setUp(self):
        """Create a sample customer for testing."""
        self.customer = Customer.objects.create(name="John Doe", balance=1000)

    def test_deposit(self):
        """Test deposit functionality."""
        self.customer.deposit(500)
        self.assertEqual(self.customer.balance, 1500)

    def test_withdraw(self):
        """Test withdraw functionality."""
        self.customer.withdraw(200)
        self.assertEqual(self.customer.balance, 800)

    def test_invalid_withdraw(self):
        """Test withdrawal when balance is insufficient."""
        self.customer.withdraw(1200)
        self.assertEqual(self.customer.balance, 1000)  # No change, because withdrawal failed


# customers/tests.py integration testing ------------------------------

from django.test import TestCase
from .models import Customer

class CustomerDatabaseIntegrationTest(TestCase):
    def setUp(self):
        """Create a customer in the database."""
        self.customer = Customer.objects.create(name="Alice", balance=500)

    def test_customer_creation(self):
        """Test if the customer was correctly saved to the database."""
        customer_from_db = Customer.objects.get(name="Alice")
        self.assertEqual(customer_from_db.balance, 500)


# Functional testing ----------------------------------------
from django.test import TestCase
from django.urls import reverse
from .models import Customer
import json

class CustomerFunctionalTest(TestCase):
    def setUp(self):
        """Create a customer in the database."""
        self.customer = Customer.objects.create(name="Bob", balance=1000)

    def test_deposit_money_api(self):
        """Test the deposit money API."""
        url = reverse('deposit_money', args=[self.customer.id])
        response = self.client.post(url, json.dumps({'amount': 500}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['new_balance'], 1500)
