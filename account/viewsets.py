from rest_framework import viewsets, permissions
from account import models, serializers


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class MenuModelViewSet(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer