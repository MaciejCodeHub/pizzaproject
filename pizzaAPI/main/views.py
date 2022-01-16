from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PizzaTypeSerializer, PizzaSerializer, OrderInfoSerializer
from .models import PizzaType, Pizza, OrderInfo


@api_view(['GET'])
def homepage(request):
    urls = {
        "": "displays urls",
        "menu": "displays menu",
        "add-pizza-type": "adds new pizza type to menu",
        "update-pizza-type/<str:pk>/": "uppdates existing pizza type to in menu",
        "delete-pizza-type/<str:pk>/": "deletes existing pizza type from menu",
        "choose-pizza/": "adds pizza to cart",
        "order/": "sends an order",
        "current-orders/": "shows current orders",
        "delete-order/": "deletes an order",
    }
    return Response(urls)


@api_view(['GET'])
def menu(request):
    pizza_types = PizzaType.objects.all()
    serializer = PizzaTypeSerializer(pizza_types, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_pizza_type(request):
    if request.user.is_superuser:
        serializer = PizzaTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("You don't have authority to add new pizza to menu.")


@api_view(['POST'])
def update_pizza_type(request, pk):
    if request.user.is_superuser:
        pizza_type = PizzaType.objects.get(id=pk)
        serializer = PizzaTypeSerializer(instance=pizza_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Pizza type updated.")
        else:
            return Response("Update failed. Invalid data.")
    else:
        return Response("You don't have authority to update pizza in menu.")


@api_view(['DELETE'])
def delete_pizza_type(request, pk):
    if request.user.is_superuser:
        pizza_type = PizzaType.objects.get(id=pk)
        pizza_type.delete()
        return Response("Pizza type deleted.")
    else:
        return Response("You don't have authority to delete this tasty pizza.")


@api_view(['POST'])
def choose_pizza(request):
    serializer = PizzaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Added pizza to your cart.")


@api_view(['POST'])
def order(request):
    serializer = OrderInfoSerializer(data=request.data)
    # pizzas = Pizza.objects.get(user=request.user)
    pizzas = Pizza.objects.all()
    serializer.pizzas = pizzas
    if serializer.is_valid():
        serializer.save()
        # Pizza.objects.filter(user=request.user).delete()
    return Response("Thank you for your order!")


@api_view(['GET'])
def current_orders(request):
    orders = OrderInfo.objects.all()
    serializer = OrderInfoSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_order(request, pk):
    if request.user.is_superuser:
        order_to_delete = OrderInfo.objects.get(id=pk)
        order_to_delete.delete()
        return Response("Order deleted.")
    else:
        return Response("You don't have authority to delete orders.")
