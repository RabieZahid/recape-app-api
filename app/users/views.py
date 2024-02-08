"""
Views for the users API.
"""
from rest_framework import generics
from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in system."""
    serializer_class = UserSerializer
