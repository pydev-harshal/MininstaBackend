from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users_app.models import User, Profile
from users_app.serailizers import UserProfileCreateSerializer

class UserProfileCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileCreateSerializer
    permission_classes = [AllowAny]