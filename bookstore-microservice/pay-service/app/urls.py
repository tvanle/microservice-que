from django.urls import path
from .views import PaymentListCreate, PaymentDetail, PaymentByOrder, PaymentByCustomer

urlpatterns = [
    path('payments/', PaymentListCreate.as_view()),
    path('payments/<int:pk>/', PaymentDetail.as_view()),
    path('payments/order/<int:order_id>/', PaymentByOrder.as_view()),
    path('payments/customer/<int:customer_id>/', PaymentByCustomer.as_view()),
]
