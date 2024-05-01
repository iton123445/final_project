from django.db import migrations, models
import datetime

def get_default_time():
    return datetime.datetime.now().time()

class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(default=get_default_time),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default=get_default_time),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
