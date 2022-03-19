from rest_framework import generics
from rest_framework.response import Response


from .serializers import PostSerializer


class PostView(generics.GenericAPIView):
    def post(self, request):
        data = {**request.data, **{"user": request.user.id}}

        serializer = PostSerializer(data=data)
        serializer.is_valid(self)
        serializer.save()

        response = {
            "text": serializer.data["text"],
        }
        return Response(response, status=201)
