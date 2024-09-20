# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import UserFeedView
from .views import LikePostView , UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested routing for comments
comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', comments_list, name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', comments_detail, name='comment-detail'),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
     path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
