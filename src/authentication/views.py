from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response


from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        password = make_password(self.request.data["password"])
        serializer.save(password=password)


class LoginView(generics.GenericAPIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(username=request.data["username"])
        user_data = UserSerializer(user).data

        response = {}
        response["user"] = user_data
        response["tokens"] = serializer.validated_data

        return Response(response, status=status.HTTP_200_OK)
