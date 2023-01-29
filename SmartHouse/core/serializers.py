from .models import ProductStat, Comment
from rest_framework import serializers


class ProductStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStat
        fields = ['products', 'name', 'number', 'price']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'date']
