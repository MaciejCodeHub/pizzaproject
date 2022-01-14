from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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
    serializer = PizzaTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
