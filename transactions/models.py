from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name='Created at'
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=False,
        verbose_name='Modified at'
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name='Active'
    )

    class Meta:
        abstract = True
        managed = True


class CreditCard(ModelBase):
    class CreditCardFlags(models.TextChoices):
        AMERICAN_EXPRESS = ('AM', 'American Express')
        ELO = ('EL', 'Elo')
        HIPERCARD = ('HC', 'Hipercard')
        MAESTRO = ('MA', 'Maestro')
        MASTERCARD = ('MC', 'Mastercard')
        VISA = ('VI', 'Visa')

    user = models.ForeignKey(
        to="account.User",
        db_column='id_user',
        on_delete=models.DO_NOTHING,
        null=False,
        verbose_name='User',
        related_name='users',
        default=1
    )
    name = models.CharField(
        db_column='tx_name',
        max_length=256,
        null=False,
        verbose_name='Name',
    )
    flag = models.CharField(
        db_column='tx_flag',
        max_length=2,
        null=False,
        choices=CreditCardFlags.choices,
        default=CreditCardFlags.MASTERCARD,
        verbose_name='Flag'
    )
    validate = models.DateField(
        db_column='dt_validate',
        null=False,
        verbose_name='Validate'
    )
    end_number = models.CharField(
        db_column='tx_end_numbers',
        max_length=4,
        null=False,
        verbose_name='End of Number'
    )
    day_expires = models.IntegerField(
        db_column='nb_day_expires',
        null=False,
        verbose_name='Day Expires'
    )

    class Meta:
        managed = True
        db_table = 'credit_card'


class Transaction(ModelBase):
    class TransactionType(models.TextChoices):
        DEBT = ('D', 'Debt')
        CREDIT = ('C', 'Credit')

    credit_card = models.ForeignKey(
        to='CreditCard',
        db_column='id_credit_card',
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='transactions'
    )
    user = models.ForeignKey(
        to='account.User',
        db_column='id_user',
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='transactions'
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=256        
    )
    description = models.CharField(
        db_column='tx_description',
        null=False,
        max_length=256
    )
    initial_date = models.DateField(
        db_column='dt_initial_date',
        null=False,
        blank=False,
        verbose_name='Initial date'
    )
    installments = models.IntegerField(
        db_column='nb_installments',
        null=False
    )
    installment_value = models.DecimalField(
        db_column='nb_installment_value',
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        verbose_name='Installment Value'
    )
    type = models.CharField(
        db_column='tx_type',
        max_length=1,
        null=False,
        choices=TransactionType.choices,
        default=TransactionType.DEBT
    )

    @property
    def type_label(self):
        return self.TransactionType(self.type).label

    class Meta:
        managed = True
        db_table = 'transaction'
    

class TransactionPortion(ModelBase):
    transaction = models.ForeignKey(
        to="Transaction",
        db_column="id_transaction",
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='transaction_portions'
    )
    amount_to_pay = models.DecimalField(
        db_column='nb_amount_to_pay',
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
        verbose_name='Amount to pay'
    )
    amount_paid = models.DecimalField(
        db_column='nb_amount_paid',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Amount Paid'
    )
    due_date = models.DateField(
        db_column='dt_due_date',
        null=False,
        blank=False
    )
    payment_date = models.DateField(
        db_column='dt_payment_date',
        null=True,
        blank=True
    )
    observation = models.CharField(
        db_column='tx_observation',
        max_length=200,
        null=True,
        blank=True
    )

    class Meta:
        managed = True
        db_table = 'transaction_portion'
