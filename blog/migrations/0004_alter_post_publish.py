# Generated by Django 4.2.5 on 2023-10-04 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 10, 4, 12, 55, 42, 764940, tzinfo=datetime.timezone.utc)),
        ),
    ]