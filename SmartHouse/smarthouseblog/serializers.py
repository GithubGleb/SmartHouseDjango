from rest_framework import serializers
from .models import Blog, Order


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'username',
            'title',
            'text',
            'date',
            'category',
            'date_publication',
            'raiting',
            'price'
        )

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'username',
            'products',
            'condition',
            'date_order',
            'total_price'
        )

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)



















