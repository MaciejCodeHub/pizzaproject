from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("menu/", views.menu, name="menu"),
    path("add-pizza-type/", views.add_pizza_type, name="add_pizza_type"),
    path("update-pizza-type/<str:pk>/", views.update_pizza_type, name="update_pizza_type"),
    path("delete-pizza-type/<str:pk>/", views.delete_pizza_type, name="delete_pizza_type"),
]
