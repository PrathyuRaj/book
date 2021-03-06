# Generated by Django 4.0.2 on 2022-04-09 14:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0014_alter_orders_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 14, 19, 38, 55, 376888), null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
