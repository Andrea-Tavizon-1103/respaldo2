from django.db import models

# Create your models here.

class Cliente(models.Model):
    ID_Cliente=models.CharField(primary_key=True, max_length=6)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=15)
    Direccion=models.CharField(max_length=100)
    Fecha_Registro=models.DateField()

    def __str__(self) :
        return self.Nombre 
