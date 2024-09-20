from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from social_media_api.posts import permissions
from .serializers import UserRegistrationSerializer, UserSerializer, PostSerializer
from .models import CustomUser, Post, Follow
from rest_framework.permissions import IsAuthenticated

# User registration (open to all users)
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]  # No authentication required for registration

# Custom token authentication
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# Follow/Unfollow views (require authentication)
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Authentication required
    queryset = CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, pk=user_id)
        request.user.following.add(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Authentication required
    queryset = CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

# User feed (requires authentication)
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authentication required

    def get_queryset(self):
        # Get posts from followed users
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# List all users (requires authentication)
class ListUsersView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Authentication required
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
