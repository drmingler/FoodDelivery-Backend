from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializer import FoodSerializer, TransactionSerializer, CreateOrderSerializer
from ..models import OrderItem, OrderDetail, Transaction, Food, Address, Customer, City
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView


def home(request):
    return HttpResponse("<p>Welcome</p>")


class AllTransactionsListView(ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class EachTransactionView(RetrieveAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()


class DeleteATransactionView(DestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class FoodListView(ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class CreateOrderView(APIView):
    serializer_class = CreateOrderSerializer

    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        street = request.data.get('street')
        postal_code = request.data.get('postal_code')
        foods = request.data.get('foods')
        print(request.data)

        if not user_name:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)

        if foods == None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)
        try:
            # Create a new address and store to database
            new_customer = Customer.objects.create(
                username=user_name,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            new_customer.save()

            # Create a new address and store to database
            city = City.objects.filter(id=1).first()
            new_address = Address.objects.create(
                city_id=city,
                customer_id=new_customer,
                street=street,
                postal_code=postal_code
            )
            new_address.save()

            new_order_details = OrderDetail.objects.create(customer_id=new_customer)
            new_order_details.save()

            # Loop through food in the food list and create an order item instance for it
            order_items = []
            for food in foods:
                new_order_item = OrderItem.objects.create(
                    order_details_id=new_order_details,
                    food_id=Food.objects.filter(id=food).first()
                                                         )
                new_order_item.save()
                order_items.append(new_order_item)

            # store the latest transaction
            new_transaction = Transaction.objects.create(order_details=new_order_details)
            new_transaction.ordered_item.add(*order_items)
            new_transaction.save()

        except Exception as e:
            print(e)
            return Response({"message": "Something went wrong request"}, status=HTTP_200_OK)

        return Response({"message": "Order Successfull"}, status=HTTP_200_OK)
