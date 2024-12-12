from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Marcas(models.Model):
    
    MARCA_CHOICES = [
        ('ford', 'Ford'),
        ('fiat', 'Fiat'),
        ('chevrolet', 'Chevrolet'),
        ('toyota', 'Toyota'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    
class Categorias(models.Model):
    
    CATEGORIA_CHOICES = [
        ('particular', 'Particular'),
        ('transporte', 'Transporte'),
        ('carga', 'Carga'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')

class Vehiculos(models.Model):
    
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, null=False)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=False)
    precio = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    
    
class CustomerUser(AbstractUser):

    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Visualizador'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='viewer')