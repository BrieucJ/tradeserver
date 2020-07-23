# Generated by Django 3.0.7 on 2020-07-22 22:20

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20200722_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 22, 20, 51, 725520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 22, 20, 51, 722010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sellorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 22, 20, 51, 724913, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='portfolio',
            unique_together={('user', 'portfolio_type')},
        ),
    ]
