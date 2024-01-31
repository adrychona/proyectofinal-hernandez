from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mascota(models.Model):
   
    def __str__(self):
        return f'{self.nombre}'
    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()


class Vacuna(models.Model):
    def __str__(self):
        return f'{self.mascota} --- {self.vacuna}'
    mascota = models.CharField(max_length=40)
    vacuna = models.CharField(max_length=40)
    fecha = models.DateField()


class Consulta(models.Model):
    def __str__(self):
        return f'{self.paciente} --- {self.fecha}'
    paciente = models.CharField(max_length=40)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    vet = models.CharField(max_length=40)
    establecimiento = models.CharField(max_length=100)

class Avatar(models.Model):
    
    #Foreign key

    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #usuario ya creado
    #Atributo

    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f'{self.usuario} --- {self.imagen}'