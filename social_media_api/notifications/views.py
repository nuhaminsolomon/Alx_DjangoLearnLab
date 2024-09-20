from django.shortcuts import render

# Create your views here.
# notifications/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer # type: ignore

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, read=False)

class NotificationReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)
        return Response({"message": "Notifications marked as read."}, status=status.HTTP_200_OK)
