from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:pk>/comments/new/'),

    path('search/', search_posts, name='search'),
    path('tags/<str:tag_name>/', TaggedPostListView.as_view(), name='tag_posts'),

    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]

from .views import register, login, logout, profile
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
