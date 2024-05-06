from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models.functions import ExtractMonth, ExtractYear, Concat

from transactions import models, serializers
from django.db.models import Max, Min, Sum, Case, When, OuterRef, F, Subquery, Value, IntegerField, ExpressionWrapper, \
    DurationField, CharField


class CreditCard:
    @staticmethod
    def get_choices():
        choices = models.CreditCard.CreditCardFlags.choices
        result = []
        for choice in choices:
            result.append({'value': choice[0], 'label': choice[1]})
        return result

    @staticmethod
    def get_current_transactions(month, year):
        cards = models.CreditCard.objects.filter(
            transactions__active=True,
            transactions__transaction_portions__due_date__month=month,
            transactions__transaction_portions__due_date__year=year
        ).annotate(
            due_date=Concat(
                Value(year), Value('-'), Value(month), Value('-'), F('day_expires'), output_field=CharField()
            )
        ).values('id', 'name', 'flag', 'validate', 'due_date', 'user_id').distinct()

        for card in list(cards):
            transactions = (models.TransactionPortion.objects
            .filter(transaction__credit_card_id=card['id'], due_date__month=month, due_date__year=year).values(
                'id', 'transaction_id', 'transaction__name', 'transaction__description', 'transaction__installments',
                'transaction__type', 'amount_to_pay', 'amount_paid', 'due_date', 'payment_date', 'observation',
                'transaction__initial_date'
            )).annotate(
                diff_months=((F('due_date__year') - F('transaction__initial_date__year')) * 12 + F(
                    'due_date__month') - F('transaction__initial_date__month')) + 1,
                current_installment=Concat(
                    F('diff_months'), Value('/'), F('transaction__installments'), output_field=CharField())
            ).order_by('due_date')

            total = 0
            for transaction in transactions:
                total += transaction['amount_to_pay']

            if transactions.exists():
                card['transactions'] = transactions
                card['total'] = total

        return cards


class TransactionAction:
    @staticmethod
    def generate_portion_transaction(transaction: 'models.Transaction'):
        for i in range(transaction.installments):
            due_date = transaction.initial_date + relativedelta(months=i)
            models.TransactionPortion.objects.create(
                amount_to_pay=transaction.installment_value,
                transaction=transaction,
                due_date=due_date
            )

    @staticmethod
    def update_portions_transaction(transaction: 'models.Transaction'):
        portions = models.TransactionPortion.objects.filter(transaction=transaction.id)
        for portion in portions:
            if portion.payment_date is None:
                portion.amount_to_pay = transaction.installment_value
                portion.save()


class TransactionPortionAction:
    @staticmethod
    def generate_months_transitions():
        months = []
        date_range = models.TransactionPortion.objects.aggregate(Max('due_date'), Min('due_date'))

        if date_range['due_date__max'] is None or date_range['due_date__min'] is None:
            return months

        diff_months = (date_range['due_date__max'].year - date_range['due_date__min'].year) * 12 + (
                date_range['due_date__max'].month - date_range['due_date__min'].month)


        for i in range(diff_months + 1):
            due_date = date_range['due_date__min'] + relativedelta(months=i)
            value = models.TransactionPortion.objects \
                .filter(due_date__year=due_date.year, due_date__month=due_date.month) \
                .aggregate(total=Sum('amount_to_pay'))

            months.append({
                "date": due_date,
                "month": due_date.strftime('%b'),
                "year": due_date.year,
                "value": value['total']
            })

        return months

    @staticmethod
    def teste(queryset):
        return queryset.values()
