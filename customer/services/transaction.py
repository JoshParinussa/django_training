from decimal import Decimal
from customer.models import Customer, Product, Transaction, Cart
from django.db.models import Sum
from customer.services import transaction


def create_customer_transaction(customer: Customer) -> Transaction:
    customerid = customer.id
    subtotal = Cart.objects.filter(customer_id=customerid).aggregate(Sum('sub_total'))
    dis = 10
    discount_trans = Decimal(dis/100)
    subtotal = subtotal.get('sub_total__sum')
    discount = subtotal * discount_trans
    grandtotal = subtotal - discount
    transaction = Transaction.objects.create(
        sub_total = subtotal,
        discount = dis,
        grand_total = grandtotal
    )
    return transaction

def get_discount_price(price: Decimal, discount: int=0) -> Decimal:
    d = discount/ Decimal(100.0)
    discount_product = price * d
    discount_price = price - discount_product
    return discount_price
    

def create_cart(customer: Customer, product: Product) -> Cart:
    subtotal = get_discount_price(product.price, product.discount)
    cart = Cart.objects.create(
        customer=customer,
        product=product,
        sub_total=subtotal,
    )
    return cart