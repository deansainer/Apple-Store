from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import routers, serializers, viewsets


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'