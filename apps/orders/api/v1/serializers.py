from rest_framework import serializers

from apps.orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'order_category',
            'contact_name',
            'contact_phone',
            'agency',
            'order_description',
            'company',
            'deadline',
            'time_until_deadline',
        ]
