# customers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('deposit/<int:customer_id>/', views.deposit_money, name='deposit_money'),
]
