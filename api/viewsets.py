from rest_framework import viewsets, mixins
from rest_framework.response import Response

from api.models import Post
from api.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer


class PostViewset(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return PostCreateSerializer
            case 'update':
                return PostUpdateSerializer
            case _:
                return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({})
