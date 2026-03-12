from django.urls import path
from .views import OrderListCreate, OrderDetail, CustomerOrders, OrderItemListCreate

urlpatterns = [
    path('orders/', OrderListCreate.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('orders/customer/<int:customer_id>/', CustomerOrders.as_view()),
    path('order-items/', OrderItemListCreate.as_view()),
]
