# Generated by Django 3.1 on 2020-08-15 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meeting', 
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
