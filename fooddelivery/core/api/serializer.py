from abc import ABC

from rest_framework import serializers
from ..models import (Customer, Country, City, Food, OrderDetail, OrderItem, Transaction)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    customerName = serializers.StringRelatedField(source='customer_id.first_name')

    class Meta:
        model = OrderDetail
        fields = ['id', 'customerName', 'order_type', 'payment_method', 'order_date', 'order_time']


class OrderItemSerializer(serializers.ModelSerializer):
    food_id = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ["id", "food_id", "quantity", "price", "totalItemPrice"]


class TransactionSerializer(serializers.ModelSerializer):
    ordered = serializers.SerializerMethodField(source='ordered')
    orderDetail = serializers.SerializerMethodField(source='orderDetail')

    class Meta:
        model = Transaction
        fields = ['id', 'ordered', 'orderDetail', 'total']

    def get_ordered(self, obj):
        return OrderItemSerializer(obj.ordered_item.all(), many=True).data

    def get_orderDetail(self, obj):
        return OrderDetailSerializer(obj.order_details).data


class CreateOrderSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    foods = serializers.ListField(child=serializers.IntegerField(),  allow_empty=True)
    city = serializers.CharField(max_length=200, default='Pecs')
    street = serializers.CharField(max_length=200, default='Pecs')
    postal_code = serializers.CharField(max_length=20)


