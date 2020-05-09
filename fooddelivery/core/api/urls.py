from django.urls import path, include
from .views import OrderItemListView


urlpatterns = [
    path('', OrderItemListView.as_view(), name="list_api_view"),
]