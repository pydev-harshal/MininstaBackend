from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from users_app import serailizers

# Create a new user account.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserCreateSerializer
    permission_classes = [permissions.AllowAny]

# Get user account details for given username.
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'

# Update account details of logged in user.
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Delete account of logged in user.
class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

