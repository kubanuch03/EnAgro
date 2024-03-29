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
<<<<<<< HEAD
=======

>>>>>>> 68af60dc5ff229e41ad615b7f20b9acb8c9b3da6


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
        query = self.request.query_params.get("search", "")
        return Category.objects.filter(name__icontains=query)



class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAdminUser,
    ]
<<<<<<< HEAD
=======

>>>>>>> 68af60dc5ff229e41ad615b7f20b9acb8c9b3da6


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
        query = self.request.query_params.get("search", "")
        return PodCategory.objects.filter(name__icontains=query)
