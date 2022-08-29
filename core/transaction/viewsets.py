from rest_framework import viewsets
from transaction import models, serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    ordering_fields = "__all__"
    ordering = ("-id",)

class TransactionViewset(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    ordering_fields = "__all__"
    ordering = ("-id",)
    