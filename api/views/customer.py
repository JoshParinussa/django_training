from rest_framework import viewsets
from api.serializers.customer import CustomerSerializer
from customer.models import Customer
from rest_framework import generics

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        
        if name:
            return Customer.objects.filter(name=name)
        else:
            return super().get_queryset()



