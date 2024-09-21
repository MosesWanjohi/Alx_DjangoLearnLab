from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Create your views here.
#Views for posts
class PostViewSet(viewsets.ModelViewSet):

    def create_post(self, request, *args, **kwargs):
        querryset = Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def list(self, request, *args, **kwargs):
        quueryset = Post.objects.all()
        serializer = PostSerializer(quueryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#comment viewsets
class CommentViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def list(self, request, *args, **kwargs):
        quueryset = Comment.objects.all()
        serializer = CommentSerializer(quueryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)