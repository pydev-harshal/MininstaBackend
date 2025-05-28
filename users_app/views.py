from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users_app.models import User, Profile
from users_app import serailizers

class UserProfileCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileCreateSerializer
    permission_classes = [AllowAny]


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileDetailView
    permission_classes = [IsAuthenticated]
    lookup_field ='username'


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileUpdateView
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserProfileDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serailizers.UserProfileDetailView
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user