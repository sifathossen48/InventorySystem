# Generated by Django 4.2 on 2023-06-28 11:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_status',
            field=models.SmallIntegerField(choices=[(0, 'In Stock'), (1, 'Out of Stock'), (2, 'Coming Soon')], default=0),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
                ('qty', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
