from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users_app.models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': False,
                'validators': [UniqueValidator(queryset=User.objects.all())]
            }
        }

    def validate_confirm_password(self, value):
        if 'password' in self.initial_data:
            if value != self.initial_data['password']:
                raise serializers.ValidationError("Passwords do not match.")
        return value
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(
            **validated_data
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['profile_photo', 'display_name', 'bio', 'following_count', 'followers_count']
    
    def get_following_count(self, instance):
        return instance.following.count()
    
    def get_followers_count(self, instance):
        return instance.user.profiles.count()
    
class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'profile']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        profile.profile_photo = profile_data.get('profile_photo') if profile_data.get('profile_photo', None) else profile.profile_photo
        profile.display_name = profile_data.get('display_name', profile.display_name)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.save()

        return instance

class UserSearchResultSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='profile.display_name')
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'display_name', 'url']