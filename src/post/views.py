from rest_framework import generics
from rest_framework.response import Response


from .serializers import CreatePostSerializer, ListPostSerializer
from .models import Post


class PostView(generics.GenericAPIView):
    def post(self, request):
        data = {**request.data, **{"user": request.user.id}}

        serializer = CreatePostSerializer(data=data)
        serializer.is_valid(self)
        serializer.save()

        return Response(serializer.data, status=201)


class PostListView(generics.ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.exclude(user=self.request.user.id)
