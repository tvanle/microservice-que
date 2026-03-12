from django.urls import path
from .views import RecommendForCustomer, RecommendationHistory, TopBooks

urlpatterns = [
    path('recommend/<int:customer_id>/', RecommendForCustomer.as_view()),
    path('recommend/<int:customer_id>/history/', RecommendationHistory.as_view()),
    path('top-books/', TopBooks.as_view()),
]
