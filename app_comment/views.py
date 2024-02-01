from .serializers import CommentSerializer, CommentRatingSerializer
from .models import Comment, CommentRating
from rest_framework.viewsets import ModelViewSet
from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView
import logging
logger = logging.getLogger(__name__)


class CreateCommentView(GenericAPIView):

    serializer_class = CommentSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            srz_data.save(
                writer=request.user,
                register_date=datetime.now(),
            )
            return Response(
                data={"message": "comment created success"},
                status=status.HTTP_201_CREATED,
            )


class CommentListView(ListAPIView):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]





class CommentDeleteApiView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        message = "успешно удалено"
        return Response(str(message), status=status.HTTP_204_NO_CONTENT)






class CommentsRatingViewSet(ListCreateAPIView):
    queryset = CommentRating.objects.all()
    serializer_class = CommentRatingSerializer

    def get_queryset(self):
        try:
            comment_id = self.kwargs['comment_id']
            return CommentRating.objects.filter(comment_id=comment_id)
        except CommentRating.DoesNotExist:
            return CommentRating.objects.none()
        except Exception as e:
            logger.error(f"Error in CommentsCourseAPIView: {e}")
            return CommentRating.objects.none()
    queryset = CommentRating.objects.none()

