from django.http import HttpResponse
from ..models import OrderItem,OrderDetail
from django.db.models import Count

def home(request):
    # query_set = OrderItem.objects.filter(order_details_id=1)
    # total=0
    # for item in query_set:
    #     total += item.get_total_item_price()
    # print(total)
    # result = OrderDetail.objects.all()
    # for item in result:
    #     print(item.quantity)
    print("I ran")


    return HttpResponse("<p>Welcome</p>")
