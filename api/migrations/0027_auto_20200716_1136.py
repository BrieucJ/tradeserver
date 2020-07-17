# Generated by Django 3.0.7 on 2020-07-16 11:36

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0026_auto_20200714_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 11, 36, 53, 572327, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 11, 36, 53, 571671, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='buyorder',
            unique_together={('user', 'price_date', 'stock', 'portfolio')},
        ),
        migrations.AlterUniqueTogether(
            name='sellorder',
            unique_together={('price_date', 'position', 'stock', 'portfolio')},
        ),
    ]
