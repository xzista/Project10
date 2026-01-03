from rest_framework import serializers
from .models import Post, Comment
from .services import validate_author_age, validate_post_title

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author",)

    def validate(self, data):
        user = self.context["request"].user
        validate_author_age(user)
        validate_post_title(data.get("title", ""))
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("author",)