from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from accounts.models import CustomUser
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

["permissions.IsAuthenticated"]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Users that the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        generics.get_object_or_404(Post, pk=pk)
        Like.objects.get_or_create(user=request.user, post=post)
        post = get_object_or_404(Post, pk=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You've already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(user=request.user, post=post)
        
        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post,
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        return Response({"detail": "Post liked successfully!"}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        generics.get_object_or_404(Post, pk=pk)
        Like.objects.get_or_create(user=request.user, post=post)
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully!"}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
