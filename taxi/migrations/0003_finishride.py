# Generated by Django 3.2 on 2021-04-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20210429_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='finishride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_num', models.CharField(max_length=10)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
