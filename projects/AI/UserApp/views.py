from tkinter import EW
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, response, request
from UserApp.serializers import CreateUserSerializer, UserSerializer
# Create your views here.


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serials = UserSerializer(users, many=True)
        return response.Response(serials.data)

    def create(self, request):
        serials = UserSerializer(data=request.POST, many=True)
        if serials.is_valid():
            if User.objects.filter(email=request.data['email']).exists():
                pass
            serials.save()
            users = User.objects.all()
            ser = UserSerializer(users)
            return response.Response(ser.data)
        else:
            return response.Response(data=serials.errors)

    def retrieve(self, request, pk=None):
        users = User.objects.get(id=pk)
        ser = UserSerializer(users)
        return response.Response(ser.data)

    def update(self, request, pk=None):
        return response.Response(data='update')

    def partial_update(self, request, pk=None):
        return response.Response(data='partial_update')

    def destroy(self, request, pk=None):
        return response.Response(data='destroy')
