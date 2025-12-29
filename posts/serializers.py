from rest_framework import serializers
from .models import Post, Comment
from .services import validate_author_age, validate_post_title

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, attrs):
        validate_author_age(attrs["author"])
        validate_post_title(attrs["title"])
        return attrs

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"