# Generated by Django 3.0.7 on 2020-07-13 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200712_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='executed_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='submited_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='order',
            constraint=models.UniqueConstraint(condition=models.Q(order_type='BUY'), fields=('price_date', 'position', 'stock'), name='order_constraint'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='executed_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='model',
        ),
        migrations.RemoveField(
            model_name='order',
            name='submit_date',
        ),
    ]
