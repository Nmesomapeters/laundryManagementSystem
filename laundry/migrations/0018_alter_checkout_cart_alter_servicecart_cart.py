# Generated by Django 5.0.4 on 2024-08-23 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0017_checkout_cart_alter_servicecart_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='laundry.cart'),
        ),
        migrations.AlterField(
            model_name='servicecart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.cart'),
        ),
    ]
