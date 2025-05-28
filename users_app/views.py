from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from users_app.models import User, Profile, UserFollow
from users_app import serailizers

class UserProfileCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileCreateSerializer
    permission_classes = [AllowAny]


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileDetailSerializer
    permission_classes = [AllowAny]
    lookup_field ='username'


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserProfileDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
            
            
class UserFollowersListView(generics.ListAPIView):
    serializer_class = serailizers.UserFollowersListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['follower__full_name', 'follower__username']

    def get_queryset(self):
        user = get_object_or_404 (User, username=self.kwargs['username'])
        return user.followers.all()


class UserFollowingListView(generics.ListAPIView):
    serializer_class = serailizers.UserFollowingListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['follower__full_name', 'follower__username']

    def get_queryset(self):
        user = get_object_or_404 (User, username=self.kwargs['username'])
        return user.following.all()
    
