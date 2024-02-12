from .serializers import CommentSerializer, CommentRatingSerializer
from .models import Comment, CommentRating
from rest_framework import generics
from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView
import logging
logger = logging.getLogger(__name__)
from app_clients.permissions import IsClientOrAdmin


class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]




class CommentListView(ListAPIView):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


class CommentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsClientOrAdmin,]
    lookup_field = "id"



class ProductCommentsApiView(ListAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            product_id = self.kwargs['product_id']
            return Comment.objects.filter(product_id=product_id)
        except Comment.DoesNotExist:
            return CommentRating.objects.none()
        except Exception as e:
            logger.error(f"Error in CommentsCourseAPIView: {e}")
            return Comment.objects.none()
    queryset = Comment.objects.none()



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






class CommentsRatingViewSet(ListAPIView):
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

class RatingCommentApiView(CreateAPIView):
    queryset = CommentRating.objects.all()
    serializer_class = CommentRatingSerializer
    permission_classes = [AllowAny, ]