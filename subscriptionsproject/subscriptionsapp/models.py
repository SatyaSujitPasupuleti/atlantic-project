from django.db import models
class Subscription(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    plan_name = models.CharField(max_length=100)
    price = models.IntegerField()
class Customer(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    subscription = models.OneToOneField(
        Subscription,
        on_delete=models.CASCADE,
        related_name="customer",
    )

class Gift(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    plan_name = models.CharField(max_length=100)
    price = models.IntegerField()
    recipient_email = models.EmailField()
    customer = models.ForeignKey(Customer,related_name='gifts',on_delete=models.CASCADE)
    
class CustomerOrder(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name="customerorder"
    )
