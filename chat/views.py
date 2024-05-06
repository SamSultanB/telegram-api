from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Contact, Profile
from .models import ChatMessage
from users.serializers import ProfileSerializer
from chat.serializers import ChatMessageSerializer
from rest_framework import status
from django.db.models import Q

@api_view(['GET', 'POST'])
def chat(request, id, idd):
    try:
        contact = Contact.objects.get(id=id)
        receiver = Contact.objects.get(id=idd)
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve all chat messages between the contact and the receiver
        chat_messages = ChatMessage.objects.filter(
            (Q(msg_sender=contact.profile) & Q(msg_receiver=receiver.profile)) |
            (Q(msg_sender=receiver.profile) & Q(msg_receiver=contact.profile))
        )
        serializer = ChatMessageSerializer(chat_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Create a new chat message
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def chatProfile(request, id, idd):

    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)