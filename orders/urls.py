from django.urls import path
from .views import MyOrderView, CreateOrderProductView, DeleteOrderProductView, update_order_product_quantity

urlpatterns = [
    path('mi-orden/', MyOrderView.as_view(), name="my-order"),
    path('agregar-producto', CreateOrderProductView.as_view(), name="add_products"),
    path('eliminar-producto/<int:pk>/', DeleteOrderProductView.as_view(), name="delete_product"),
    path('update-quantity/', update_order_product_quantity, name='update_quantity'),
]
