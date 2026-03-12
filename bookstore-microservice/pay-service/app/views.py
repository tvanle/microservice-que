from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreate(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        return Response(PaymentSerializer(payments, many=True).data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetail(APIView):
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return None

    def get(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(PaymentSerializer(payment).data)

    def put(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentByOrder(APIView):
    def get(self, request, order_id):
        payments = Payment.objects.filter(order_id=order_id)
        return Response(PaymentSerializer(payments, many=True).data)

class PaymentByCustomer(APIView):
    def get(self, request, customer_id):
        payments = Payment.objects.filter(customer_id=customer_id)
        return Response(PaymentSerializer(payments, many=True).data)
