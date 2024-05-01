# Generated by Django 5.0.4 on 2024-05-01 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_booking_bike_alter_booking_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(default='01:17:35.937885'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default='01:17:35.937885'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.bike'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.customer'),
        ),
    ]
