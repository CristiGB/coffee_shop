from django.urls import path
from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name="my-order"),
    path('agregar-producto', CreateOrderProductView.as_view(), name="add_products")
]
