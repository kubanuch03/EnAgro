from django.urls import path
from .views import LikeView

urlpatterns = [
    path('create/list/', LikeView.as_view(), name='like-product-get-post'),
    # path('dislike/', DisLikeView.as_view(), name='dislike-product'),
    # path('favorite/products/', FavoriteProductsView.as_view(), name='favorite-products'),
]
