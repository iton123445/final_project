# Generated by Django 5.0.4 on 2024-05-01 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_booking_end_time_booking_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.bike'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(default='00:56:50.165858'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default='00:56:50.165858'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.bike')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.customer')),
            ],
        ),
    ]
