# Generated by Django 4.0.5 on 2023-08-29 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ESTUDIANTE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(max_length=25)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('estado_civil', models.CharField(max_length=20)),
                ('N_documento', models.CharField(max_length=15)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('nacimiento_fecha', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('especialidad', models.CharField(max_length=200)),
                ('tiene_discapacidad', models.CharField(max_length=10)),
                ('tipo_discapacidad', models.CharField(max_length=50)),
                ('carnet_discapacidad', models.CharField(max_length=15)),
                ('estado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to='PROFESORES')),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.etnia')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.genero')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.tipo_documento')),
                ('tipo_sangre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.tipo_sangre')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profesor_cur_materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('curso_paralelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.curso_paralelo')),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.jornada')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROFESOR.materia')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.periodo')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROFESOR.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('registro', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.jornada')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROFESOR.materia')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.matricula')),
                ('trimestre_parcial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ESTUDIANTE.trimestre_parcial')),
            ],
        ),
    ]
