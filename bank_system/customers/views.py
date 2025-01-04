from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def deposit_money(request, customer_id):
    """API to deposit money into a customer's account."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = data.get('amount', 0)
            customer = Customer.objects.get(id=customer_id)
            customer.deposit(amount)
            return JsonResponse({"success": True, "new_balance": int(customer.balance)})  # Return as integer
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Customer not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=400)

    