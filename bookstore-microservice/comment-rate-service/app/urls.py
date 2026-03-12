from django.urls import path
from .views import CommentListCreate, CommentsByBook, CommentDetail, RatingListCreate, RatingsByBook

urlpatterns = [
    path('comments/', CommentListCreate.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('comments/book/<int:book_id>/', CommentsByBook.as_view()),
    path('ratings/', RatingListCreate.as_view()),
    path('ratings/book/<int:book_id>/', RatingsByBook.as_view()),
]
