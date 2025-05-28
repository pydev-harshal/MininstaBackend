from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from users_app.models import User,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']


class UserProfileCreateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'password', 'profile']
        extra_kwargs = {
            'username': {'validators': [UnicodeUsernameValidator()]},
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if User.objects.filter(username=value.lower()).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user
    