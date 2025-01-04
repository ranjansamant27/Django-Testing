from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def deposit(self, amount):
        """Method to deposit money into the customer's account."""
        if amount > 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        """Method to withdraw money from the customer's account."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.save()
