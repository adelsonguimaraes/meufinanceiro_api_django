from tkinter import CASCADE
from django.db import models
from transaction.enums import ActiveEnum, TransactionTypeEnum


class BaseModel (models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        blank=False,
        null=False
    )
    active = models.BooleanField(
        db_column='cs_active',
        blank=False,
        null=False,
        choices=ActiveEnum.choices,
        default=ActiveEnum.ACTIVE
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now=False,
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        db_column='update_at',
        auto_now=True,
        auto_now_add=False
    )

    class Meta:
        abstract = True


class User (BaseModel):
    name = models.CharField(
        max_length=254  ,
        db_column='tx_name',
        null=False,
        blank=False
    )
    email = models.EmailField(
        db_column='tx_email',
        max_length=254,
        blank=False,
        null=False
    )
    password = models.CharField(
        db_column='tx_password',
        max_length=254,
        blank=False,
        null=False
    )
    

class Transaction (BaseModel):
    user = models.ForeignKey(
        to=User,
        db_column='id_user',
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING
    )
    description = models.CharField(
        db_column='tx_description',
        max_length=200,
        blank=False,
        null=False
    )
    value = models.FloatField(
        db_column='nb_value',
        blank=False,
        null=False,
        default=0
    )
    type = models.CharField(
        db_column='tx_type',
        max_length=3,
        blank=False,
        null=False,
        default=TransactionTypeEnum.DEBIT,
        choices=TransactionTypeEnum.choices
    )
    expiration_day = models.IntegerField(
        db_column='nb_expiration_day',
        blank=False,
        null=False
    )
    installments = models.IntegerField(
        db_column='nb_installments',
        blank=True,
        null=True,
        default=0
    )

    class Meta:
        db_table = 'transaction'
        managed = True


class TransactionsInstallments(BaseModel):
    transaction = models.ForeignKey(
        to='transaction.Transaction',
        db_column='id_transaction',
        on_delete=models.CASCADE
    )
    duedate = models.DateField(
        db_column='dt_duedate',
        auto_now=False,
        auto_now_add=False,
        blank=False,
        null=False
    )
    payday = models.DateField(
        db_column='dt_payday',
        auto_now=False,
        auto_now_add=False,
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'transaction_installments'
        managed = True
