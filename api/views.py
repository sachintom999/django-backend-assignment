from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers


@api_view(["POST"])
def signup(request):
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


@api_view(["POST"])
def login(request):
    user = User.objects.filter(username=request.data["username"]).first()
    if user:
        if user.check_password(request.data["password"]):
            return Response({"message": "login success"})
        else:
            return Response({"message": "login failed"})
    else:
        return Response({"message": "User not found!"})


@api_view(["GET"])
def getPosts(request):
    posts = models.Post.objects.all()
    serializer = serializers.PostSerializer(posts, many=True)
    return Response(serializer.data)
