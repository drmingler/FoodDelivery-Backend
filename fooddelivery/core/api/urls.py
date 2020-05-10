from django.urls import path, include
from .views import AllTransactionsListView, EachTransactionView, FoodListView, CreateOrderView, DeleteATransactionView

urlpatterns = [
    path('foods/', FoodListView.as_view(), name="all_foods_api_view"),
    path('transaction/<int:pk>', EachTransactionView.as_view(), name="each_transaction_api_view"),
    path('transactions/', AllTransactionsListView.as_view(), name="all_transactions_api_view"),
    path('create/', CreateOrderView.as_view(), name="create_order_api"),
    path('delete/<int:pk>', DeleteATransactionView.as_view(), name="delete_order_api"),
]