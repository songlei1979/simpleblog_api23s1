from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def create(self, request):
#         return self.create(request)
#
# class PostDetail(GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def destroy(self, request, id):
#         return self.destroy(request, id=id)
#
