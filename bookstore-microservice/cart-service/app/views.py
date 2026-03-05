from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
import requests

BOOK_SERVICE_URL = "http://book-service:8000"

class CartCreate(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCartItem(APIView):
    def post(self, request):
        book_id = request.data.get("book_id")

        # Verify book exists in book-service
        try:
            r = requests.get(f"{BOOK_SERVICE_URL}/books/")
            books = r.json()
            if not any(b["id"] == book_id for b in books):
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.ConnectionError:
            return Response({"error": "Book service unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewCart(APIView):
    def get(self, request, customer_id):
        try:
            cart = Cart.objects.get(customer_id=customer_id)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
