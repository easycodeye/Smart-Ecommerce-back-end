from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework import viewsets, response, request, views, permissions, authentication
from UserApp.serializers import CreateUserSerializer, UserSerializer
from rest_framework.authtoken.models import Token
# Create your views here.


class UserModelsViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        users = User.objects.all()
        serials = UserSerializer(users, many=True)
        return response.Response(serials.data)

    def create(self, request):
        serials = UserSerializer(data=request.POST, many=True)
        if serials.is_valid():
            user = User.objects.get(username=request.data['username'])
            if user:
                login(request=request, user=user)
            else:
                user = serials.save()
                login(request=request, user=user)

            token = Token.objects.get_or_create(user=user)
            return response.Response(data=[token[0].key, UserSerializer(user).data])
        else:
            return response.Response(data=serials.errors)

    def retrieve(self, request, pk=None):
        users = User.objects.get(id=pk)
        ser = UserSerializer(users)
        return response.Response(ser.data)

    def update(self, request, pk=None):
        serials = UserSerializer(data=request.POST)
        if serials.is_valid():
            serials.update()
        return response.Response(serials.data)

    def partial_update(self, request, pk=None):
        return response.Response(data='partial_update')

    def destroy(self, request, pk=None):
        logout(request=request)
        return response.Response(data='done')
