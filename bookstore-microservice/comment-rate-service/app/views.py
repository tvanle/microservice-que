from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer

class CommentListCreate(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        return Response(CommentSerializer(comments, many=True).data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsByBook(APIView):
    def get(self, request, book_id):
        comments = Comment.objects.filter(book_id=book_id)
        return Response(CommentSerializer(comments, many=True).data)

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if not comment:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RatingListCreate(APIView):
    def get(self, request):
        ratings = Rating.objects.all()
        return Response(RatingSerializer(ratings, many=True).data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingsByBook(APIView):
    def get(self, request, book_id):
        ratings = Rating.objects.filter(book_id=book_id)
        avg = ratings.aggregate(average=Avg('score'))['average']
        return Response({
            "book_id": book_id,
            "ratings": RatingSerializer(ratings, many=True).data,
            "average_score": round(avg, 2) if avg else None,
        })
