from django.urls import path
from .views import LikeView, DisLikeView,FavoriteProductsView

urlpatterns = [
    path('like/', LikeView.as_view(), name='like-product'),
    path('dislike/', DisLikeView.as_view(), name='dislike-product'),
    path('favorite-products/', FavoriteProductsView.as_view(), name='favorite-products'),
]

