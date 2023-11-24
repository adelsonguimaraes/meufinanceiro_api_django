# Generated by Django 4.2.1 on 2023-07-10 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', verbose_name='Modified at')),
                ('active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Active')),
                ('name', models.CharField(db_column='tx_name', max_length=256, verbose_name='Name')),
                ('flag', models.CharField(choices=[('AL', 'Alelo'), ('AM', 'American Express'), ('EL', 'Elo'), ('HC', 'Hipercard'), ('MA', 'Maestro'), ('MC', 'Mastercard'), ('SO', 'Sodexo'), ('VI', 'Visa'), ('FL', 'Flash')], db_column='tx_flag', default='MC', max_length=2, verbose_name='Flag')),
                ('validate', models.DateField(db_column='dt_validate', verbose_name='Validate')),
                ('end_number', models.CharField(db_column='tx_end_numbers', max_length=4, verbose_name='End of Number')),
                ('day_expires', models.IntegerField(db_column='nb_day_expires', verbose_name='Day Expires')),
            ],
            options={
                'db_table': 'credit_card',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='transactionportion',
            name='observation',
            field=models.CharField(blank=True, db_column='tx_observation', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='credit_card',
            field=models.ForeignKey(db_column='id_credit_card', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='transactions.creditcard'),
        ),
    ]