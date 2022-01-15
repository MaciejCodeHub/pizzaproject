from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PizzaTypeSerializer
from .models import PizzaType


@api_view(['GET'])
def homepage(request):
    urls = {
        "": "displays urls",
        "menu": "displays menu",
        "add-pizza-type": "adds new pizza type to menu",
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
