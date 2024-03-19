# Generated by Django 3.2.23 on 2024-01-30 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100)),
                ('trn_no', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('trn_type', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('openingbalance', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('payment', models.CharField(blank=True, max_length=100, null=True)),
                ('current_date', models.DateField(blank=True, max_length=255, null=True)),
                ('End_date', models.CharField(blank=True, max_length=255, null=True)),
                ('additionalfield1', models.CharField(blank=True, max_length=100, null=True)),
                ('additionalfield2', models.CharField(blank=True, max_length=100, null=True)),
                ('additionalfield3', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField(blank=True, default=0, null=True)),
                ('billdate', models.DateField()),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('VAT', models.CharField(default=0, max_length=100, null=True)),
                ('taxamount', models.CharField(default=0, max_length=100, null=True)),
                ('adjust', models.CharField(default=0, max_length=100, null=True)),
                ('grandtotal', models.FloatField(default=0, null=True)),
                ('advance', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.CharField(blank=True, max_length=255, null=True)),
                ('tot_bill_no', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.party')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=20)),
                ('transactiondate', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('purchasebill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.purchasebill')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('VAT', models.CharField(max_length=100)),
                ('discount', models.CharField(default=0, max_length=100, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.item')),
                ('purchasebill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.purchasebill')),
            ],
        ),
    ]