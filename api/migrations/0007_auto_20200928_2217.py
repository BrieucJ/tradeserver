# Generated by Django 3.0.7 on 2020-09-28 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200927_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexhistory',
            options={'ordering': ['-price_date']},
        ),
    ]
