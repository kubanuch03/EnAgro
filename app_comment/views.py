from .serializers import CommentSerializer
from .models import Comment

from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response






class CreateCommentView(GenericAPIView):
    """
        create new comment for product
    """

    serializer_class = CommentSerializer

    permission_classes = (
        IsAuthenticated,
    )

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                writer=request.user,
                register_date=datetime.now(),
            )
            return Response(data={'message': 'comment created success'}, status=status.HTTP_201_CREATED)


class CommentListView(GenericAPIView):
    """
        show list of confirmed comments
    """

    serializer_class = CommentSerializer
    queryset = Comment.confirmed.all()
    permission_classes = (
        AllowAny,
    )

    def get(self, request):
        comments = Comment.confirmed.all()
        srz_data = self.serializer_class(instance=comments, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)