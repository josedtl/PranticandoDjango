from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Catalogo_TipoDocumento(models.Model):
    TipodocumentoId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class Catalogo_Persona(models.Model):
    PersonaId = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipodocumentoId = models.ForeignKey(
        Catalogo_TipoDocumento, on_delete=models.CASCADE
    )


class Cabecera(models.Model):
    CabeceraId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)


class Detalle(models.Model):
    detalleId = models.AutoField(primary_key=True)
    CabeceraId = models.ForeignKey(Cabecera, on_delete=models.CASCADE, related_name='detalles')
    Nombre = models.CharField(max_length=100)

class CabeceraProfesores(models.Model):
    Nombre = models.CharField(max_length=100)

class DetalleAlumnos(models.Model):
    Nombre = models.CharField(max_length=100)
    cabecera = models.ForeignKey(CabeceraProfesores, on_delete=models.CASCADE, related_name='detalles')