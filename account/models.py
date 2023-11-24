from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_column='tx_username',
        null=False,
        max_length=64,
        unique=True
    )
    password = models.CharField(
        db_column='tx_password',
        null=False,
        max_length=104
    )
    name = models.CharField(
        db_column='tx_name',
        null=True,
        max_length=256
    )
    email = models.CharField(
        db_column='tx_email',
        null=False,
        blank=False,
        max_length=256,
        unique=True
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        null=False,
        default=True
    )
    is_staff = models.BooleanField(
        db_column='cs_staff',
        null=False,
        default=False
    )
    is_default = models.BooleanField(
        db_column='cs_default',
        null=False,
        default=False
    )
    avatar = models.BinaryField(
        db_column='bl_avatar',
        null=True
    )
    is_ad_user = models.BooleanField(
        db_column='cs_ad_user',
        null=False,
        default=False
    )
    is_privileged_user = models.BooleanField(
        db_column='cs_privileged_user',
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


class Menu(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    description = models.CharField(
        db_column='tx_description',
        max_length=64,
        blank=True,
        null=True
    )
    icon = models.CharField(
        db_column='tx_icon',
        max_length=64,
        blank=True,
        null=False
    )
    route = models.CharField(
        db_column='tx_route',
        max_length=64,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.description} - {self.route}"
    
    class Meta:
        managed = True
        db_table = 'account_menu'


class UserMenu(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    user = models.ForeignKey(
        to='User',
        db_column='id_user',
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='user_menus'
    )
    menu = models.ForeignKey(
        to='Menu',
        db_column='id_menu',
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='user_menus'
    )

    class Meta:
        db_table = 'account_user_menu'
        managed = True
        unique_together = [('user', 'menu')]
