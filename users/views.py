from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UsersSerializer, ProfileSerializer, ContactSerializer
from .models import Users, Profile, Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    
    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT'])
def profile(request, id):

    profile = Profile.objects.get(id = id)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def contacts(request, id):

    profile = Profile.objects.get(id = id)

    if request.method == 'GET':
        serializer = ContactSerializer(profile.contacts.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)