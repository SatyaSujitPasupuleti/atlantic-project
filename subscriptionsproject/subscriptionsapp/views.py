from django.shortcuts import render
from subscriptionsproject.subscriptionsapp.models import Customer
from rest_framework import viewsets
from .serializers import (
    CustomerSerializer
)

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

