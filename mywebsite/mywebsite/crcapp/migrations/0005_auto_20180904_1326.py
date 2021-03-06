# Generated by Django 2.0.7 on 2018-09-04 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crcapp', '0004_auto_20180904_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='id',
        ),
        migrations.AddField(
            model_name='orders',
            name='Car_ID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='crcapp.Car'),
        ),
        migrations.AddField(
            model_name='orders',
            name='Customer_ID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='crcapp.Customer'),
        ),
        migrations.AddField(
            model_name='orders',
            name='Order_ReturnDate',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='store',
            name='Store_ID',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer_ID',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_ID',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_ReturnStore',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='crcapp.Store'),
        ),
    ]
