from django.contrib import admin
from .models import Customer, Country, City, Address, Food, OrderDetail, OrderItem, Transaction


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username',
                    'first_name',
                    'last_name',
                    'phone_number',
                    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer_id',
                    'city_id',
                    'street',
                    'postal_code',
                    ]


class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name',
                    ]


class CityAdmin(admin.ModelAdmin):
    list_display = ['country_id',
                    'city_name',
                    ]


class FoodAdmin(admin.ModelAdmin):
    list_display = ['food_name',
                    'food_description',
                    'price',
                    ]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['customer_id',
                    'order_type',
                    'payment_method',
                    'order_date',
                    'order_time',
                    'shipping_address'
                    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_details_id',
                    'food_id',
                    'quantity',
                    'totalItemPrice'
                    ]


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
                    'order_details'
                    ]


admin.site.register(Customer, CustomerAdmin),
admin.site.register(Country, CountryAdmin),
admin.site.register(City, CityAdmin),
admin.site.register(Address, AddressAdmin),
admin.site.register(Food, FoodAdmin),
admin.site.register(OrderDetail, OrderDetailAdmin),
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Transaction,TransactionAdmin),
