from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("menu/", views.menu, name="menu"),
    path("add-pizza-type/", views.add_pizza_type, name="add_pizza_type"),
    path("update-pizza-type/<str:pk>/", views.update_pizza_type, name="update_pizza_type"),
    path("delete-pizza-type/<str:pk>/", views.delete_pizza_type, name="delete_pizza_type"),
    path("choose-pizza/", views.choose_pizza, name="choose_pizza"),
    path("order/", views.order, name="order"),
    path("current-orders/", views.current_orders, name="current_orders"),
    path("delete-order/<str:pk>/", views.delete_order, name="delete_order"),
]
