from django.urls import path, include
from app_products.views import ProductDetailView, ProductListApiView, ProductCreateApiView, ProductsByCategoryApiView, ProductsByPodCategoryApiView



urlpatterns = [
    path('categories/<int:category_id>/products/', ProductsByCategoryApiView.as_view(), name='products_by_category'),
    path('podcategory/<int:podcategory_id>/products/', ProductsByPodCategoryApiView.as_view(), name='products_by_podcategory'),
    path("product/list/", ProductListApiView.as_view(), name="product-list"),
    path('product/create/', ProductCreateApiView.as_view(), name='product-create'),
    path("product/detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
