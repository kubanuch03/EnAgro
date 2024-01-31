from django.urls import path
from .views import CreateCommentView, CommentListView, CommentDeleteApiView

urlpatterns = [
    path("list/comments/", CommentListView.as_view(), name="list_of_comment"),
    path("create/comments/", CreateCommentView.as_view(), name="create_comment"),
    path("delete/comments/<int:pk>/", CommentDeleteApiView.as_view(), name='delete_comments'),
]
