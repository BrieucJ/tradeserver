# Generated by Django 3.0.7 on 2020-09-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediction',
            old_name='model',
            new_name='neural_network',
        ),
        migrations.AddField(
            model_name='neuralnetwork',
            name='future_target',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='neuralnetwork',
            name='prediction_type',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='neuralnetwork',
            name='target_type',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together={('price_date', 'stock', 'neural_network')},
        ),
    ]