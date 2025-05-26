from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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