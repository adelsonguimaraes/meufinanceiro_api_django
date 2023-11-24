from rest_framework import serializers
from account import models
from rest_flex_fields import FlexFieldsModelSerializer


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'name',
            'username',
            'email',
            'last_login',
            'is_active',
            'is_superuser',
            'is_staff',
            'is_default',
            'avatar',
            'is_ad_user',
            'is_privileged_user'
        ]

    expandable_fields = {
        'menus': ('account.MenuSerializer', {'source': 'user_menus', 'many': True})
    }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = [
            'description',
            'icon',
            'route'
        ]