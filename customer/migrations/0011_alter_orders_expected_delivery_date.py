# Generated by Django 4.0.3 on 2022-04-06 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_orders_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 11, 14, 23, 57, 621952), null=True),
        ),
    ]
