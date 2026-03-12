from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import Counter
import requests
from .models import Recommendation
from .serializers import RecommendationSerializer

COMMENT_RATE_SERVICE_URL = "http://comment-rate-service:8000"
BOOK_SERVICE_URL = "http://book-service:8000"

class RecommendForCustomer(APIView):
    """
    Recommends books to a customer based on top-rated books
    excluding books they have already rated.
    """
    def get(self, request, customer_id):
        try:
            # Fetch all ratings
            r = requests.get(f"{COMMENT_RATE_SERVICE_URL}/ratings/", timeout=5)
            all_ratings = r.json()
        except Exception:
            all_ratings = []

        # Count ratings per book
        book_scores = Counter()
        rated_by_customer = set()
        for rating in all_ratings:
            book_id = rating.get("book_id")
            score = rating.get("score", 0)
            book_scores[book_id] += score
            if rating.get("customer_id") == customer_id:
                rated_by_customer.add(book_id)

        # Top 5 books not yet rated by this customer
        recommended_ids = [
            book_id for book_id, _ in book_scores.most_common(20)
            if book_id not in rated_by_customer
        ][:5]

        # Save recommendation record
        rec = Recommendation.objects.create(
            customer_id=customer_id,
            book_ids=recommended_ids,
            reason="Based on highest community ratings"
        )

        return Response({
            "customer_id": customer_id,
            "recommended_book_ids": recommended_ids,
            "reason": rec.reason,
        })

class RecommendationHistory(APIView):
    def get(self, request, customer_id):
        recs = Recommendation.objects.filter(customer_id=customer_id).order_by('-created_at')
        return Response(RecommendationSerializer(recs, many=True).data)

class TopBooks(APIView):
    """Returns top-rated books regardless of customer."""
    def get(self, request):
        try:
            r = requests.get(f"{COMMENT_RATE_SERVICE_URL}/ratings/", timeout=5)
            all_ratings = r.json()
        except Exception:
            all_ratings = []

        book_scores = Counter()
        for rating in all_ratings:
            book_scores[rating.get("book_id")] += rating.get("score", 0)

        top_ids = [book_id for book_id, _ in book_scores.most_common(10)]
        return Response({"top_book_ids": top_ids})
