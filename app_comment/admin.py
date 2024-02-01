from django.contrib import admin
from .models import Comment, CommentRating


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentRating)
class AdminComment(admin.ModelAdmin):
    pass
