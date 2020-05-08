from django.contrib import admin
from .models import Customer, Country, City, Address, Food, OrderDetail, OrderItem


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
                    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_details_id',
                    'food_id',
                    'quantity',
                    ]


admin.site.register(Customer, CustomerAdmin),
admin.site.register(Country),
admin.site.register(City),
admin.site.register(Address),
admin.site.register(Food),
admin.site.register(OrderDetail),
admin.site.register(OrderItem),
