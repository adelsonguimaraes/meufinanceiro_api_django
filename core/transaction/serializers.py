from rest_framework import serializers
from transaction import models

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

class TransactionSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"