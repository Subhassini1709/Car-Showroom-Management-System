# Generated by Django 4.0.1 on 2022-11-16 13:57

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userrent_uimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcar',
            name='RImage',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.filepath),
        ),
    ]
