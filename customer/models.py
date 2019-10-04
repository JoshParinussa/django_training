from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True)
    City = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name        = models.CharField(max_length=50)
    price       = models.DecimalField(max_digits=20, decimal_places=2)
    discount    = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Cart(models.Model):

    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    sub_total   = models.DecimalField(max_digits=20, decimal_places=2)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, blank=True, null=True, related_name='carts')

    def __str__(self):
        return f'{self.customer.name} : {self.product.name} : {self.created}'

class Transaction(models.Model):

    transaction_date    = models.DateTimeField(auto_now_add=True)
    sub_total           = models.DecimalField(max_digits=20, decimal_places=2)
    discount            = models.PositiveSmallIntegerField(default=0)
    grand_total         = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.id}'