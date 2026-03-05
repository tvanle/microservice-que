from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('cart/<int:customer_id>/', views.view_cart, name='view_cart'),
]
