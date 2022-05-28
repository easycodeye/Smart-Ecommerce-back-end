from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

from UserApp.models import BirthDate, UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class BirthDateSerializer(serializers.Serializer):
    class Meta:
        model = BirthDate
        fields = '__all__'


class UserTypeSerializer(serializers.Serializer):
    class Meta:
        model = UserType
        fields = '__all__'
