from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreateView, CategoryDetailView, PodCategoryViewSet

router = DefaultRouter()
router.register(r"pod/category", PodCategoryViewSet, basename="PodCategory")


urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("", include(router.urls))
    # Другие URL, если необходимо
]
