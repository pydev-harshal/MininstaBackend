from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from users_app import serailizers


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserCreateSerializer
    permission_classes = [permissions.AllowAny]
