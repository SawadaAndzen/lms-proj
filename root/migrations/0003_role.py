# Generated by Django 4.2.17 on 2025-01-16 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0002_alter_profile_pfp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')], max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
