from django.shortcuts import render
import requests

BOOK_SERVICE_URL = "http://book-service:8000"
CART_SERVICE_URL = "http://cart-service:8000"

def book_list(request):
    try:
        r = requests.get(f"{BOOK_SERVICE_URL}/books/")
        books = r.json()
    except requests.exceptions.ConnectionError:
        books = []
    return render(request, "books.html", {"books": books})

def view_cart(request, customer_id):
    try:
        r = requests.get(f"{CART_SERVICE_URL}/carts/{customer_id}/")
        items = r.json()
    except requests.exceptions.ConnectionError:
        items = []
    return render(request, "cart.html", {"items": items})
