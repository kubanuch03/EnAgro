from rest_framework import serializers
from app_comment.models import Comment, CommentRating


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'product', 'photo1','photo2','photo3','photo4', 'body']


class CommentRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentRating
        fields = ['id', 'comment', 'rating', 'user'] 