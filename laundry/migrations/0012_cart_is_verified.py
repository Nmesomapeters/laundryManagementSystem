# Generated by Django 5.0.4 on 2024-05-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0011_cart_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
