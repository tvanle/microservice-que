from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/comments/', views.book_comments, name='book_comments'),
    path('top-books/', views.top_books, name='top_books'),
    path('cart/<int:customer_id>/', views.view_cart, name='view_cart'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/customer/<int:customer_id>/', views.customer_orders, name='customer_orders'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('recommend/<int:customer_id>/', views.recommend_books, name='recommend_books'),
    path('staff/', views.staff_list, name='staff_list'),
    path('managers/', views.manager_list, name='manager_list'),
]
