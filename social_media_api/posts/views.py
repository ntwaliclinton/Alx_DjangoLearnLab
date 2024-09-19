from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post  # assuming a Post model exists
from .serializers import PostSerialize
from rest_framework.response import Response
from rest_framework import status
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Assuming Post has a 'created_at' field
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    # Get the users the current user is following
    followed_users = request.user.following.all()
    
    # Get posts from followed users, ordered by creation date
    posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')
    
    # Serialize and return posts (you would need to have a serializer for Post)
    serialized_posts = PostSerializer(posts, many=True)  # PostSerializer should be created for this
    return Response(serialized_posts.data, status=status.HTTP_200_OK)