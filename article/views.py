from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import post
from rest_framework import serializers
from rest_framework import status


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model= post
        fields = "__all__"

@api_view(['GET'])
def getAllArticle(request):
    allpost = post.objects.filter(active = True).all().order_by("dateCreated")
    converted_data = articleSerializer(allpost, many = True)
    return Response(converted_data.data)

@api_view(['GET'])
def getArticle (reqest, id):
    Post= post.objects.filter(id = id).first()
    converted_data = articleSerializer(Post)

    return Response(data = converted_data.data)

@api_view(['POST'])
def  createArticle(request):
    serializers = articleSerializer(data = request.data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_200_OK )
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
