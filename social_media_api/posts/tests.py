from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_post(self):
        response = self.client.post(reverse('post-list'), {'title': 'Test Post', 'content': 'Content'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)

    # Add more tests for update, delete, and filtering

