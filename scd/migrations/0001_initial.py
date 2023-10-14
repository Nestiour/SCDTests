# Generated by Django 4.2.1 on 2023-09-27 00:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_cur', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.CharField(max_length=1)),
                ('division', models.CharField(max_length=1)),
                ('especialidad', models.CharField(max_length=15)),
                ('turno', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('cuil', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('domicilio', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=1)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_hor', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=1)),
                ('h_i', models.CharField(max_length=1)),
                ('h_f', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_mat', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='doc_mat',
            fields=[
                ('id_dm', models.AutoField(primary_key=True, serialize=False)),
                ('id_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.docente')),
                ('id_mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id_cla', models.AutoField(primary_key=True, serialize=False)),
                ('id_cur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.curso')),
                ('id_dm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.doc_mat')),
                ('id_hor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.horario')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asi', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('asistencia', models.CharField(max_length=1)),
                ('articulo', models.CharField(blank=True, max_length=20)),
                ('id_cla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scd.clase')),
            ],
        ),
    ]