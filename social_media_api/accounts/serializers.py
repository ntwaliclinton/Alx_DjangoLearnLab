from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()
serializers.CharField() 
Token.objects.create 
get_user_model().objects.create_user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        return user
from rest_framework import serializers
from .models import CustomUser

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'following']
