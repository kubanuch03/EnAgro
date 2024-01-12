from django.urls import path
from .views import ProductDetailView

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]