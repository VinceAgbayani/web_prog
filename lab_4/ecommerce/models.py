from django.db import models

# Create your models here.

class AbstractClass(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	class Meta:
		abstract = True

class User(AbstractClass):
	email = models.EmailField()
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	shipping_address = models.TextField()

	def __str__(self):
		return self.first_name + " " + self.last_name

class Product(AbstractClass):
	price = models.FloatField()
	name = models.CharField(max_length = 20)
	description = models.TextField()

	def __str__(self):
		return self.name

class Cart(AbstractClass):
	cart_code = models.CharField(max_length = 10)
	total_price = models.FloatField()
	product = models.ManyToManyField(Product)
	has_paid = models.BooleanField()

from Cart.models import PaidCarts
PaidCarts.objects.allfilter(paid_exact=True)

from Cart.models import UnpPaidCarts
PaidCarts.objects.allfilter(paid_exact=False)