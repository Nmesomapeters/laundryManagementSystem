# Generated by Django 5.0.4 on 2024-08-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0019_remove_checkout_status_checkout_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
