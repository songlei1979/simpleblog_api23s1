from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer, UserSerializer


@api_view(['GET'])
def index(request):
    # if request.user.is_authenticated:
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return HttpResponse(serializer.data)
    # return HttpResponse("Hello nobody")

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = PostSerializer(instance=post)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        post.delete()
        return Response("Deleted")

@api_view(['GET', ])
def get_user_id(request):
    try:
        return Response(request.user.id)
    except:
        return Response(None)




