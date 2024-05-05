from rest_framework import serializers
from .models import Users, Profile, Contact
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Users
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Profile
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Contact
        fields = '__all__'