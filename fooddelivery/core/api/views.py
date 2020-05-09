from django.http import HttpResponse

from .serializer import OrderItemSerializer
from ..models import OrderItem, OrderDetail
from rest_framework.generics import ListAPIView


def home(request):
    # query_set = OrderItem.objects.filter(order_details_id=1)
    # total=0
    # for item in query_set:
    #     total += item.get_total_item_price()
    # print(total)

    return HttpResponse("<p>Welcome</p>")


class OrderItemListView(ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
