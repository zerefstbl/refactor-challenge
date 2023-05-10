from rest_framework import viewsets, permissions, status

from apps.orders.models import Order
from apps.orders.api.v1.serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Order.objects.all()
