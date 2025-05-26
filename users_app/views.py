from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from users_app import serailizers

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'username', 'email', 'profile__display_name']

