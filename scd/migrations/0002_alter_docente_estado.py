# Generated by Django 4.2.1 on 2023-09-27 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='estado',
            field=models.CharField(max_length=8),
        ),
    ]
