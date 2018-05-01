from ecommerce.models import User, Product, Cart
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'firstName', 'lastName', 'shippingAddress')


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('price', 'name', 'description')

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = ('cart_code', 'totalPrice', 'product', 'hasPaid')