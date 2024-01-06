from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


# Представление для получения списка и создания новых категорий
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Представление для получения деталей, обновления и удаления категории
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Представление для получения списка и создания новых продуктов
