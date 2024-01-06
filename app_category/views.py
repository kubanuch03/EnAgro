from rest_framework import generics
from .models import Category, PodCategory
from .serializers import CategorySerializer, PodCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


# Представление для получения списка и создания новых категорий
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        return Category.objects.filter(name__icontains=query)


# Представление для получения деталей, обновления и удаления категории
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Представление для получения списка и создания новых продуктов
class PodCategoryViewSet(ModelViewSet):
    queryset = PodCategory.objects.all()
    serializer_class = PodCategorySerializer
    permission_classes = [
        AllowAny,
    ]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name", "category"]

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        return PodCategory.objects.filter(name__icontains=query)
