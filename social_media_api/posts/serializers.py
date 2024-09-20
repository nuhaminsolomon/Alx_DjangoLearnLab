from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Include author details, read-only

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the logged-in user
        post = Post.objects.create(author=user, **validated_data)
        return post

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Include author details, read-only
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Ensure the post exists

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the logged-in user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment
