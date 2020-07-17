# Generated by Django 3.0.7 on 2020-07-13 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 13, 31, 4, 733012, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 13, 31, 4, 729679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 13, 31, 4, 732376, tzinfo=utc)),
        ),
    ]
