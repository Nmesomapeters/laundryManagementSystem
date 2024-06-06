# Generated by Django 5.0.4 on 2024-05-24 17:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0009_remove_transaction_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='clothes_amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='clothes_type',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='num_dresses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='num_others',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='num_pants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='num_shirts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='num_skirts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='num_suits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pickup_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
