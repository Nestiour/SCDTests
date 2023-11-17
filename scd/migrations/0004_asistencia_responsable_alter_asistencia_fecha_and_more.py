# Generated by Django 4.2.1 on 2023-10-19 01:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scd', '0003_alter_docente_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='responsable',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='id_cla',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scd.clase'),
        ),
    ]
