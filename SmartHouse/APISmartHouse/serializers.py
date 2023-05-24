
from rest_framework import serializers
from smarthouseblog.models import Blog, Order, Cart
from core.models import New_profile


class BlogSerializerForTitle(serializers.ModelSerializer):
    class Meta:
        model = Blog

        fields = ('title',)


class NewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_profile

        fields = ('username',)


class BlogSerializer(serializers.ModelSerializer):
    username = NewListSerializer()

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
    username = NewListSerializer()

    products = BlogSerializerForTitle(many=True)

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


class CartSerializer(serializers.ModelSerializer):

    product = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cart
        fields = ('product',)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        cart = Cart.objects.filter(username__username=validated_data['user']).first()
        if cart:
            cart.product.add(validated_data['product'])
        if not cart:
            user = New_profile.objects.filter(username=validated_data['user']).first()
            cart = Cart.objects.create(username=user)
            cart.product.add(validated_data['product'])
        return cart