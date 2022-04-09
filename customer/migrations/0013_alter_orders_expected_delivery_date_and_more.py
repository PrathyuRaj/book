# Generated by Django 4.0.3 on 2022-04-07 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_books_image'),
        ('customer', '0012_alter_orders_expected_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 12, 11, 30, 16, 622216), null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.books'),
        ),
    ]
