# Generated by Django 5.0.7 on 2024-07-24 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StravaToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
    ]
