# Generated by Django 4.2.5 on 2023-10-04 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 10, 4, 10, 5, 29, 38918, tzinfo=datetime.timezone.utc)),
        ),
    ]
