# Generated by Django 5.0.7 on 2024-07-23 17:34

import django.db.models.deletion
import phonenumber_field.modelfields
import src.admins.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='No information provided for this country')),
                ('is_available_for_sender', models.BooleanField(default=False)),
                ('is_available_for_receiver', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/gifts/')),
                ('commission', models.FloatField(default=1.1, help_text='Commission for Red Sparrow services')),
                ('description', models.TextField(default='No information provided for this gift')),
                ('price', models.FloatField(default=100)),
            ],
            options={
                'verbose_name_plural': 'Gift Cards',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('charges', models.FloatField(default=0)),
                ('description', models.CharField(default='Description not provided yet.', max_length=100)),
                ('is_figure', models.BooleanField(default=False, help_text='Figure means not in %')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(default=src.admins.models.default_generate_key, max_length=2000)),
                ('receiver_first_name', models.CharField(max_length=10)),
                ('receiver_last_name', models.CharField(max_length=10)),
                ('receiver_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('total_amount', models.FloatField(default=0)),
                ('tax_charges', models.FloatField(default=0)),
                ('fees_charges', models.FloatField(default=0)),
                ('payable_amount', models.FloatField(default=0)),
                ('stripe_pay_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(choices=[('unp', 'Un Paid'), ('pai', 'Paid'), ('fai', 'Failed'), ('pen', 'Pending'), ('com', 'Completed'), ('can', 'Cancelled')], default='unp', max_length=3)),
                ('is_customized', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('closed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to=settings.AUTH_USER_MODEL)),
                ('gift_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admins.giftcard')),
                ('receiver_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_country', to='admins.country')),
                ('sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admins.paymentmethod')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'ordering': ['created_on', 'status'],
            },
        ),
    ]
