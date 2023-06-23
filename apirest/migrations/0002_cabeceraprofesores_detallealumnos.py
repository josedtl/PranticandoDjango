# Generated by Django 4.2.2 on 2023-06-22 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabeceraProfesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAlumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('cabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='apirest.cabeceraprofesores')),
            ],
        ),
    ]