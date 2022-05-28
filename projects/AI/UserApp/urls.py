
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from UserApp.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'',UserViewSet,basename='user')



urlpatterns = [
    path('',include(router.urls)),
]
