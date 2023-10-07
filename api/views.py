from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, serializers


@api_view(["POST"])
def register(request):
    """User registration view"""
    try:
        # check if the username already exists
        user = User.objects.filter(username=request.data["username"]).first()
        # if exists, return appropriate message
        if user:
            return Response(
                {"message": "Username already exists"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        # else, proceed with user creation
        else:
            serializer = serializers.UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(username=request.data["username"])
                user.set_password(request.data["password"])
                user.save()
                return Response(
                    {"message": "User registered successfully","username":user.username},
                    status=status.HTTP_201_CREATED,
                )
    except Exception as e:
        return Response(
            {"message": "Registration failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class CreatePostView(CreateAPIView):
    """View for creating a new post"""

    serializer_class = serializers.PostSerializer
    permission_classes = [
        IsAuthenticated
    ]  # this makes sure only authenticated users can create a post

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )  # we pass only the post title and content in the request, author field is populated from the details in JWT token
