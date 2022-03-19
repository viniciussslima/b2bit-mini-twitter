from mmap import PAGESIZE
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user", "text"]


class ListPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ["id", "user", "text"]
