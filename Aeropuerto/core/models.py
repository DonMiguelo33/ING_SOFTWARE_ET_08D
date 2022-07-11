from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self): 
        return self.nombreCategoria

class Chofer (models.Model): 
    nombre = models.CharField(max_length=70, verbose_name='Nombre')
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    numero = models.CharField(max_length=50, verbose_name='Numero')
    patente = models.CharField(max_length=7, verbose_name='Patente')
    estacionamiento = models.CharField(max_length=50, verbose_name='Estacionamiento')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.rut

class Pasajero (models.Model): 
    nombre = models.CharField(max_length=70, verbose_name='Nombre')
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    hora = models.CharField(max_length=13, verbose_name='Hora')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.rut