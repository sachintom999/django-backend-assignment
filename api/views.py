from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, serializers


@api_view(["POST"])
def register(request):
    try:
        user = User.objects.filter(username=request.data["username"]).first()
        if user:
            return Response({"message": "Username already exists"})
        else:
            serializer = serializers.UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(username=request.data["username"])
                user.set_password(request.data["password"])
                user.save()
                return Response({"message": "User registered successfully"})
    except Exception as e:
        print(e)
        return Response({"message": "Registration failed"})


class CreatePostView(CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
