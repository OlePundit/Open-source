from rest_framework import generics, permissions
from .models import Post
from django.contrib.auth import get_user_model  # Import the user model

from .serializers import PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add this line to enforce authentication

    def perform_create(self, serializer):
        # Set the user field to the current authenticated user before saving
        serializer.save(user=self.request.user)
