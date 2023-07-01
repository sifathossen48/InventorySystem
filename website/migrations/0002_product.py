# Generated by Django 4.2 on 2023-06-26 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock_status', models.SmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
    ]