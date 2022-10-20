# Generated by Django 3.2.16 on 2022-10-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_carrera_escuela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id_asignatura',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='id_clase',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='id_carrera',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id_carrera'),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='id_seccion',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]