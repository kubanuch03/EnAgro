from django.urls import path, include

from .views import (CreateCommentView, CommentListView, 
CommentDeleteApiView, CommentsRatingViewSet,
CommentDetailView, RatingCommentApiView, 
ProductCommentsApiView
)


urlpatterns = [
    path("list/comment/", CommentListView.as_view(), name="list_of_comment"),
    path("product/comment/<int:product_id>/", ProductCommentsApiView.as_view(), name='комментарии определеного продукта'),
    path("create/comment/", CreateCommentView.as_view(), name="create_comment"),
    path("delete/comment/<int:pk>/", CommentDeleteApiView.as_view(), name='delete_comments'),
    path('detal/comment/<int:id>/', CommentDetailView.as_view()),
    path("rating/comment/<int:comment_id>/", CommentsRatingViewSet.as_view(), name="list_rating_comments"),
    path("rating/comment/create/", RatingCommentApiView.as_view(), name='create_comment_rating'),
]
