from django.urls import path
from .views import CategoryListCreate, CategoryDetail, BookCatalogListCreate, BooksByCategory

urlpatterns = [
    path('categories/', CategoryListCreate.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('catalog/', BookCatalogListCreate.as_view()),
    path('categories/<int:category_id>/books/', BooksByCategory.as_view()),
]
