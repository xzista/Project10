from rest_framework import serializers

from .models import Comment, Post
from .services import validate_author_age, validate_post_title


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("author",)


class CommentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "author", "text", "created_at")


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text", "author", "created_at")


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author",)

    def validate(self, data):
        user = self.context["request"].user
        validate_author_age(user)
        validate_post_title(data.get("title", ""))
        return data
