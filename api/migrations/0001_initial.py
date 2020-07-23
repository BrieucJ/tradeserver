# Generated by Django 3.0.7 on 2020-07-23 03:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_type', models.BooleanField(default=False)),
                ('currency', models.CharField(default='€', max_length=1)),
                ('cash', models.FloatField(default=None, null=True)),
                ('total_invested_value', models.FloatField(default=None, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 7, 23, 3, 57, 38, 285638, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('user', 'portfolio_type')},
            },
        ),
        migrations.CreateModel(
            name='SMABacktest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precision', models.FloatField(default=0)),
                ('score', models.FloatField(default=0)),
                ('sharpe_ratio', models.FloatField(default=0)),
                ('data_size', models.IntegerField(default=0)),
                ('stock_return', models.FloatField(default=0)),
                ('stock_cagr', models.FloatField(default=0)),
                ('stock_sd', models.FloatField(default=0)),
                ('model_return', models.FloatField(default=0)),
                ('model_cagr', models.FloatField(default=0)),
                ('model_sd', models.FloatField(default=0)),
                ('buy_count', models.IntegerField(default=0)),
                ('profitable_buy_count', models.IntegerField(default=0)),
                ('unprofitable_buy_count', models.IntegerField(default=0)),
                ('sell_count', models.IntegerField(default=0)),
                ('stop_loss_count', models.IntegerField(default=0)),
                ('take_profit_count', models.IntegerField(default=0)),
                ('max_drawdown', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='SMAModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_sma', models.IntegerField(default=10)),
                ('high_sma', models.IntegerField(default=34)),
                ('stop_loss', models.FloatField(default=0.1)),
                ('take_profit', models.FloatField(default=0.25)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['symbol'],
                'unique_together': {('symbol',)},
            },
        ),
        migrations.CreateModel(
            name='SMAPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_date', models.DateField(default=None)),
                ('buy', models.BooleanField(default=None, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sma_position', to='api.SMAModel')),
                ('sma_backtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sma_position', to='api.SMABacktest')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sma_position', to='api.Stock')),
            ],
            options={
                'ordering': ['-price_date'],
                'unique_together': {('price_date', 'stock', 'model')},
            },
        ),
        migrations.AddField(
            model_name='smabacktest',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backtest', to='api.SMAModel'),
        ),
        migrations.AddField(
            model_name='smabacktest',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backtest', to='api.Stock'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broker_username', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True))),
                ('broker_password', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_date', models.DateField(default=None)),
                ('invest_value', models.FloatField(default=0)),
                ('invest_units', models.IntegerField(default=0)),
                ('open_rate', models.FloatField(default=0)),
                ('current_rate', models.FloatField(default=0)),
                ('stop_loss_rate', models.FloatField(default=0)),
                ('take_profit_rate', models.FloatField(default=0)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='api.Portfolio')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='api.Stock')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='smabacktest',
            unique_together={('model', 'stock')},
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_shares', models.IntegerField(default=None)),
                ('price_date', models.DateField(default=None)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 7, 23, 3, 57, 38, 288409, tzinfo=utc))),
                ('submited_at', models.DateTimeField(default=None, null=True)),
                ('executed_at', models.DateTimeField(default=None, null=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to='api.Portfolio')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to='api.Position')),
                ('sma_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to='api.SMAPosition')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to='api.Stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'position', 'stock', 'portfolio')},
            },
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
                'ordering': ['-price_date'],
                'unique_together': {('stock', 'price_date')},
            },
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_date', models.DateField(default=None)),
                ('num_of_shares', models.IntegerField(default=None)),
                ('order_price', models.FloatField(default=None, null=True)),
                ('current_price', models.FloatField(default=None, null=True)),
                ('total_investment', models.FloatField(default=None, null=True)),
                ('stop_loss', models.FloatField(default=None, null=True)),
                ('take_profit', models.FloatField(default=None, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 7, 23, 3, 57, 38, 289011, tzinfo=utc))),
                ('submited_at', models.DateTimeField(default=None, null=True)),
                ('executed_at', models.DateTimeField(default=None, null=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_order', to='api.Portfolio')),
                ('sma_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_order', to='api.SMAPosition')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_order', to='api.Stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'stock', 'portfolio')},
            },
        ),
    ]
