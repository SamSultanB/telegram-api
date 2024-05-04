from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsersSerializer
from .models import Users

class UsersModelViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
