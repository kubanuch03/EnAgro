from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "writer",
            "product",
            "sub_comment",
            "body",
            "register_date",
        )

        read_only_fields = (
            "writer",
            "register_date",
            "writer",
            "product",
            "sub_comment",
            "body",
            "register_date",
        )

        read_only_fields = (
            "writer",
            "register_date",
        )
