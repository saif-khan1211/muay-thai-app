# Generated by Django 4.2.14 on 2024-08-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparring', '0003_alter_sparring_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparring',
            name='date',
            field=models.DateField(),
        ),
    ]
