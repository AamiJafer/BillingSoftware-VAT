# Generated by Django 3.2.25 on 2024-03-13 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_party_purchasebill_purchasebillitem_purchasebilltransactionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partystatus', models.CharField(blank=True, max_length=100, null=True)),
                ('returndate', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('adjustment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grandtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creditnote_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_no', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('vat', models.CharField(default=0, max_length=100, null=True)),
                ('adjustment', models.CharField(default=0, max_length=100)),
                ('grandtotal', models.FloatField(default=0, null=True)),
                ('total_taxamount', models.CharField(default=0, max_length=100)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.employee')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.item')),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='at_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='party',
            name='opening_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Transactions_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_type', models.CharField(max_length=255)),
                ('trans_number', models.CharField(max_length=255)),
                ('trans_date', models.DateTimeField()),
                ('total', models.CharField(max_length=255)),
                ('balance', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('party', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.party')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(max_length=255)),
                ('done_by_name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.employee')),
                ('salesinvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.salesinvoice')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('tax', models.CharField(blank=True, max_length=255, null=True)),
                ('totalamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.employee')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.item')),
                ('salesinvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.salesinvoice')),
            ],
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.party'),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PartyTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('transactiondate', models.DateField(auto_now=True)),
                ('Transactions_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.transactions_party')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('party', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.party')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditNoteReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='billapp.creditnote')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditNoteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255, null=True)),
                ('hsn', models.CharField(blank=True, max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('tax', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='billapp.creditnote')),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditNoteHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=20)),
                ('hist_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.company')),
                ('credit_note_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_note', to='billapp.creditnote')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='creditnote',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.party'),
        ),
        migrations.AddField(
            model_name='creditnote',
            name='salesinvoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.salesinvoice'),
        ),
        migrations.AddField(
            model_name='creditnote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
