from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        followed_users = user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]





    