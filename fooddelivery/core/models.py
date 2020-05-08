from django.db import models


# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=250, verbose_name="First name")
    last_name = models.CharField(max_length=250, verbose_name="Last name")
    phone_number = models.CharField(max_length=12, blank=True)


class Address(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city_id = models.ForeignKey("City", on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Addresses'


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'


class City(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Cities'


class Food(models.Model):
    food_name = models.CharField(max_length=250)
    food_description = models.TextField()
    price = models.FloatField()


class OrderDetail(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=30, default="Delivery")
    payment_method = models.CharField(max_length=30, default="Card")
    order_date = models.DateField(auto_now_add=True)
    order_time = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order_details_id = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
