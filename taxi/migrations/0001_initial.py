# Generated by Django 3.2 on 2021-04-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taxis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_num', models.CharField(max_length=10)),
                ('rate', models.FloatField()),
                ('avail', models.CharField(choices=[('Yes', 'No'), ('yes', 'no')], max_length=3)),
                ('driver_name', models.CharField(max_length=20)),
                ('driver_no', models.IntegerField()),
            ],
        ),
    ]
