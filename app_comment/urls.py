from django.urls import path
from .views import CreateCommentView, CommentListView

urlpatterns = [
    path("aa/", CommentListView.as_view(), name="list_of_comment"),
    path("add/", CreateCommentView.as_view(), name="create_comment"),
]

