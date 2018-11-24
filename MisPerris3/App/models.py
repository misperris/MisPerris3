from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    fecha=models.DateField()
    region=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=20)
    vivienda=models.CharField(max_length=20)
    rol=models.CharField(max_length=10, default="Normal")

class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=20)
    estado=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='db_fotos', blank=True, null=True)

    