from abc import ABC

from rest_framework import serializers
from transactions import models
from rest_flex_fields import FlexFieldsModelSerializer


class CreditCardSerializer(FlexFieldsModelSerializer):
    flag_label = serializers.ReadOnlyField(source='get_flag_display')

    class Meta:
        model = models.CreditCard
        fields = '__all__'

    expandable_fields = {
        'transactions': (
            'transactions.TransactionSerializer',
            {'many': True}
        ),
    }


class TransactionSerializer(FlexFieldsModelSerializer):
    type_label = serializers.ReadOnlyField()

    class Meta:
        model = models.Transaction
        fields = '__all__'

    expandable_fields = {
        'credit_card': (
            'transactions.CreditCardSerializer',
        ),
        'portions': (
            'transactions.TransactionPortionSerializer',
            {'source': 'transaction_portions', 'many': True}
        )
    }


class TransactionPortionSerializer(FlexFieldsModelSerializer):

    expandable_fields = {
        'transaction': (
            'transactions.TransactionSerializer',
            {'many': False}
        )
    }

    class Meta:
        model = models.TransactionPortion
        fields = '__all__'
