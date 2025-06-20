from django.shortcuts import get_object_or_404
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from users_app.models import User, Profile, UserFollow

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


class UserProfileDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)
    following_count = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'profile', 'followers_count', 'following_count', 'is_following']
    
    def get_is_following(self, instance):
        print(self.context)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return UserFollow.objects.filter(follower=request.user, following=instance).exists()
        return False
    
    def get_followers_count(self, instance):
        return instance.followers.count()

    def get_following_count(self, instance):
        return instance.following.count()


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'profile']
        extra_kwargs = {
            'username': {'validators': [UnicodeUsernameValidator()]}
        }

    def validate_username(self, value):
        user = self.instance 
        if User.objects.exclude(pk=user.pk).filter(username=value.lower()).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value
    
    def validate_email(self, value):
        user = self.instance 
        if User.objects.exclude(pk=user.pk).filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    
    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        profile.profile_photo = profile_data.get('profile_photo') if profile_data.get('profile_photo', None) else profile.profile_photo
        profile.bio = profile_data.get('bio', profile.bio)
        profile.save()

        return instance


class UserFollowersListSerializer(serializers.ModelSerializer):
    follower = UserProfileDetailSerializer(read_only=True)

    class Meta:
        model = UserFollow
        fields = ['follower']


class UserFollowingListSerializer(serializers.ModelSerializer):
    following = UserProfileDetailSerializer(read_only=True)
    
    class Meta:
        model = UserFollow
        fields = ['following']