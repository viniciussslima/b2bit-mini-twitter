from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

from .models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        password = make_password(self.request.data["password"])
        serializer.save(password=password)
        serializer.save()
