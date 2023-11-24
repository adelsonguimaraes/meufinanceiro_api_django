# Generated by Django 4.2.1 on 2023-06-22 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', verbose_name='Modified at')),
                ('active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=256)),
                ('description', models.CharField(db_column='tx_description', max_length=256)),
                ('initial_date', models.DateField(db_column='dt_initial_date', verbose_name='Initial date')),
                ('installments', models.IntegerField(db_column='nb_installments')),
                ('installment_value', models.DecimalField(db_column='nb_installment_value', decimal_places=2, default=0, max_digits=10, verbose_name='Installment Value')),
                ('type', models.CharField(choices=[('D', 'Debt'), ('C', 'Credit')], db_column='tx_type', default='D', max_length=1)),
                ('user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransactionPortion',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', verbose_name='Modified at')),
                ('active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('amount_to_pay', models.DecimalField(db_column='nb_amount_to_pay', decimal_places=2, default=0, max_digits=10, verbose_name='Amount to pay')),
                ('amount_paid', models.DecimalField(blank=True, db_column='nb_amount_paid', decimal_places=2, max_digits=10, null=True, verbose_name='Amount Paid')),
                ('due_date', models.DateField(db_column='dt_due_date')),
                ('payment_date', models.DateField(blank=True, db_column='dt_payment_date', null=True)),
                ('transaction', models.ForeignKey(db_column='id_transaction', on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_portions', to='transactions.transaction')),
            ],
            options={
                'db_table': 'transaction_portion',
                'managed': True,
            },
        ),
    ]