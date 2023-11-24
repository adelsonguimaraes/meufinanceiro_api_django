from rest_framework.routers import DefaultRouter
from account import viewsets

routers = DefaultRouter()
routers.register(r'user', viewsets.UserModelViewSet)
routers.register(r'menu', viewsets.MenuModelViewSet)

urlpatterns = routers.urls
