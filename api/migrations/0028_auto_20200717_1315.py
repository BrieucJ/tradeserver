# Generated by Django 3.0.7 on 2020-07-17 13:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200716_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 13, 15, 44, 598122, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 13, 15, 44, 597304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellorder',
            name='position',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to='api.Position'),
        ),
    ]
