# Generated by Django 3.0.7 on 2020-06-09 17:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TradingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('initial_balance', models.IntegerField(default=10000)),
                ('end_balance', models.IntegerField(default=0)),
                ('look_back', models.IntegerField(default=10)),
                ('low_sma', models.IntegerField(default=10)),
                ('high_sma', models.IntegerField(default=34)),
                ('max_single_pos', models.FloatField(default=0.1)),
                ('trading_interval', models.IntegerField(default=1)),
                ('sma_diff', models.FloatField(default=0)),
                ('sma_slope', models.FloatField(default=0)),
                ('start_date', models.DateField(default=None)),
                ('end_date', models.DateField(default=None)),
                ('max_drawdown', models.FloatField(default=0)),
                ('max_gain', models.FloatField(default=0)),
                ('true_trading_period', models.FloatField(default=0)),
                ('average_buy_pct', models.FloatField(default=0)),
                ('annualized_return', models.FloatField(default=0)),
                ('SP_return', models.FloatField(default=0)),
                ('alpha', models.FloatField(default=0)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_date', models.DateField(default=None)),
                ('open', models.FloatField(default=0)),
                ('high', models.FloatField(default=0)),
                ('low', models.FloatField(default=0)),
                ('close', models.FloatField(default=0)),
                ('volume', models.BigIntegerField(default=0)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_history', to='api.Stock')),
            ],
            options={
                'unique_together': {('stock', 'price_date')},
            },
        ),
    ]