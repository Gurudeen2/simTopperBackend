# Generated by Django 4.2.1 on 2023-09-23 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='date_fund',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 23, 16, 26, 59, 662527)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='userId',
            field=models.CharField(max_length=20),
        ),
    ]
