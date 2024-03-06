from rest_framework import serializers
from app_comment.models import Comment

from app_users.models import CustomUser



class CommentListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username')
    full_name = serializers.CharField(source='author.full_name')
    avatar = serializers.CharField(source='author.avatar')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'product', 
                'photo1','photo2','photo3',
                'photo4', 'body', 'rating', 
                'username', 'full_name', 'avatar'
]


class CommentCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'author', 'product', 'photo1','photo2','photo3','photo4', 'body', 'rating']
