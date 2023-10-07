from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model"""

    class Meta:
        model = models.Post
        fields = "__all__"
        read_only_fields = ["author"]


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""

    class Meta:
        model = models.User
        fields = "__all__"
