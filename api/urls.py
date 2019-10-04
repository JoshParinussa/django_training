from django.conf.urls import url, include
from rest_framework import routers
from api.views.customer import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]