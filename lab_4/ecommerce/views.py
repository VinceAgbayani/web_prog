from django.http import HttpResponse, JsonResponse
from ecommerce.models import User, Product, Cart
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .serialize import UserSerializer, ProductSerializer, CartSerializer

class UserView(APIView):
	def get(self, request):
		users = User.objects.all()
		serialized_account = UserSerializer(data=users, many=True)
		return JsonResponse(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class ProductView(APIView):
	def get(self, request):
		products = Product.objects.all()
		serialized_account = ProductSerializer(data=products, many=True)
		return JsonResponse(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = ProductSerializer(data=data) 
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class CartView(APIView):
	def get(self, request):
		carts = Cart.objects.all()
		serialized_account = CartSerializer(data=carts, many=True)
		return JsonResponse(serialized_account.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = CartSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)