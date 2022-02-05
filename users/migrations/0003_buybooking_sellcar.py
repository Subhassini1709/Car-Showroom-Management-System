# Generated by Django 3.2 on 2022-02-05 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20220205_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SBrandName', models.CharField(max_length=100)),
                ('SCarName', models.CharField(max_length=100)),
                ('SCarPrice', models.IntegerField()),
                ('KmRun', models.IntegerField()),
                ('CarAge', models.IntegerField()),
                ('SFuel', models.CharField(max_length=100)),
                ('SMileage', models.FloatField()),
                ('SSeatingCapacity', models.IntegerField()),
                ('SPhoneNum', models.BigIntegerField()),
                ('SAddress', models.TextField()),
                ('SCustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BAddress', models.TextField()),
                ('BPhoneNumber', models.BigIntegerField()),
                ('BBrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.buybrand')),
                ('BCarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.buycar')),
                ('BCustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
