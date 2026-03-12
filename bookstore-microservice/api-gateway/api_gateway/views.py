from django.shortcuts import render
import requests

BOOK_SERVICE_URL = "http://book-service:8000"
CART_SERVICE_URL = "http://cart-service:8000"
CUSTOMER_SERVICE_URL = "http://customer-service:8000"
CATALOG_SERVICE_URL = "http://catalog-service:8000"
ORDER_SERVICE_URL = "http://order-service:8000"
SHIP_SERVICE_URL = "http://ship-service:8000"
PAY_SERVICE_URL = "http://pay-service:8000"
COMMENT_RATE_SERVICE_URL = "http://comment-rate-service:8000"
RECOMMENDER_SERVICE_URL = "http://recommender-ai-service:8000"
STAFF_SERVICE_URL = "http://staff-service:8000"
MANAGER_SERVICE_URL = "http://manager-service:8000"


def _get_json(url, default):
    try:
        r = requests.get(url, timeout=5)
        return r.json()
    except Exception:
        return default


def book_list(request):
    books = _get_json(f"{BOOK_SERVICE_URL}/books/", [])
    categories = _get_json(f"{CATALOG_SERVICE_URL}/categories/", [])
    return render(request, "books.html", {"books": books, "categories": categories})


def view_cart(request, customer_id):
    items = _get_json(f"{CART_SERVICE_URL}/carts/{customer_id}/", [])
    return render(request, "cart.html", {"items": items, "customer_id": customer_id})


def customer_list(request):
    customers = _get_json(f"{CUSTOMER_SERVICE_URL}/customers/", [])
    return render(request, "customers.html", {"customers": customers})


def order_list(request):
    orders = _get_json(f"{ORDER_SERVICE_URL}/orders/", [])
    return render(request, "orders.html", {"orders": orders})


def customer_orders(request, customer_id):
    orders = _get_json(f"{ORDER_SERVICE_URL}/orders/customer/{customer_id}/", [])
    return render(request, "orders.html", {"orders": orders, "customer_id": customer_id})


def shipment_list(request):
    shipments = _get_json(f"{SHIP_SERVICE_URL}/shipments/", [])
    return render(request, "shipments.html", {"shipments": shipments})


def payment_list(request):
    payments = _get_json(f"{PAY_SERVICE_URL}/payments/", [])
    return render(request, "payments.html", {"payments": payments})


def book_comments(request, book_id):
    comments = _get_json(f"{COMMENT_RATE_SERVICE_URL}/comments/book/{book_id}/", [])
    ratings = _get_json(f"{COMMENT_RATE_SERVICE_URL}/ratings/book/{book_id}/", {})
    return render(request, "comments.html", {"comments": comments, "ratings": ratings, "book_id": book_id})


def recommend_books(request, customer_id):
    data = _get_json(f"{RECOMMENDER_SERVICE_URL}/recommend/{customer_id}/", {})
    book_ids = data.get("recommended_book_ids", [])
    # Fetch book details for each recommended id
    all_books = _get_json(f"{BOOK_SERVICE_URL}/books/", [])
    recommended = [b for b in all_books if b.get("id") in book_ids]
    return render(request, "recommendations.html", {"books": recommended, "customer_id": customer_id})


def staff_list(request):
    staff = _get_json(f"{STAFF_SERVICE_URL}/staff/", [])
    return render(request, "staff.html", {"staff": staff})


def manager_list(request):
    managers = _get_json(f"{MANAGER_SERVICE_URL}/managers/", [])
    return render(request, "managers.html", {"managers": managers})


def top_books(request):
    data = _get_json(f"{RECOMMENDER_SERVICE_URL}/top-books/", {})
    book_ids = data.get("top_book_ids", [])
    all_books = _get_json(f"{BOOK_SERVICE_URL}/books/", [])
    top = [b for b in all_books if b.get("id") in book_ids]
    return render(request, "books.html", {"books": top, "title": "Top Rated Books"})
