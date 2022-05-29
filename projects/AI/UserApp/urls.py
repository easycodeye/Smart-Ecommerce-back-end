
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
afrom UserApp.views import UserModelsViewSets, UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
