# Generated by Django 4.0.5 on 2023-11-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESTUDIANTE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
