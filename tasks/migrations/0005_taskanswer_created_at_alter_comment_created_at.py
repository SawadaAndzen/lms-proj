# Generated by Django 4.2.17 on 2025-02-07 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskanswer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 15, 3, 38, 248668, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 15, 3, 38, 249667, tzinfo=datetime.timezone.utc)),
        ),
    ]
