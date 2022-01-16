from rest_framework import serializers
from .models import PizzaType, Pizza, OrderInfo


class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ["name", "sauce", "size"]


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = ["address", "phone", "card_payment", "remarks"]
