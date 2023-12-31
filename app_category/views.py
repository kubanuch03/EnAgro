from rest_framework.generics import ListAPIView, CreateAPIView
from app_category.models import Category, PodCategory
from .serializers import CategorySerializer, PodCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAdminUser,
    ]


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        AllowAny,
    ]
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
    permission_classes = [
        IsAdminUser,
    ]


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
