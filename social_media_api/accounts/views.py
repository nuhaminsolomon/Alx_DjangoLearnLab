from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,get_user_model
from rest_framework import status, generics,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer, TokenSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.exceptions import NotFound

User = get_user_model()

#user = get_user_model().objects.get(username='myusername')
#token, created = Token.objects.get_or_create(user=user)



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Create user with hashed password
            user = get_user_model().objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response({
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({"detail": "Now following the user."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise NotFound("User not found.")

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": "Unfollowed the user."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise NotFound("User not found.")







