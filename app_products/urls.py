from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_products.views import ProductDetailView, ProductListApiView, ProductCreateApiView, RetingViewSet

router = DefaultRouter()
router.register(r'rating/product', RetingViewSet, basename='rating')


urlpatterns = [
    path("product/list/", ProductListApiView.as_view(), name="product-list"),
    path('product/create/', ProductCreateApiView.as_view(), name='product-create'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("", include(router.urls)),
]
