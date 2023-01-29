from .models import ProductStat
from rest_framework import serializers


class ProductStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStat
        fields = ['products', 'name', 'number', 'price']
