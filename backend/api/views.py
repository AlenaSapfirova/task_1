from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import PostPermission


class PostAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)

    def get(self, request):
        query = Post.objects.all()
        serializer = PostSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        author = request.user
        serializer = PostSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id, author=request.user)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        post = get_object_or_404(Post, id=id, author=request.user)
        if post.author == request.user:
            serializer = PostSerializer(post, data=request.data,
                                        partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'пользователь не является авторм поста'},
                        status=status.HTTP_400_BAD_REQUEST)


class RegisterApiView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
