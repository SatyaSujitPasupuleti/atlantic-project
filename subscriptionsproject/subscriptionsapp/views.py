from django.shortcuts import render
from subscriptionsproject.subscriptionsapp.models import Customer,CustomerOrder
from rest_framework import viewsets
from .serializers import (
    CustomerSerializer,
    CustomerOrderSerializer
)

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

class CustomerOrderView(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer