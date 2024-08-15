from .models import Comment, Category, Post
from rest_framework import serializers
from ..user.serializers import UserRegisterSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'user']


class CategorySerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'post', 'content', 'category', 'created_at', 'updated_at']
