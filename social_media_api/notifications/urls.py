# notifications/urls.py
from django.urls import path
from .views import NotificationListView, NotificationReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/read/', NotificationReadView.as_view(), name='notification-read'),
]
