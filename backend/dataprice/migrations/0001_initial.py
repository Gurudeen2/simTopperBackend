# Generated by Django 4.2.1 on 2023-08-24 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('networkprovider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networkprovider.networkprovider')),
            ],
        ),
    ]