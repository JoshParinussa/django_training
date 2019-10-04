from django.contrib import admin

from customer.models import Customer, Product, Cart, Transaction

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cart, CartAdmin)

class TransactionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transaction, TransactionAdmin)


