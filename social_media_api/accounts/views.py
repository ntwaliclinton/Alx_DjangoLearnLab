from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework import generics
from .models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import FollowSerializer

class FollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        request.user.follow(user_to_follow)
        return Response({"detail": "User followed successfully"}, status=status.HTTP_200_OK)

class UnfollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"detail": "User unfollowed successfully"}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(user=response.data['user_id'])
        return Response({'token': token.key})



