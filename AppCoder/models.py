from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Perro(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()
    
    def __str__(self):
        return f"Nombre:{self.name} - Raza {self.raza} - Edad{self.edad}"
class Gato(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()
    def __str__(self):
        return f"Nombre:{self.name} - Raza {self.raza} - Edad{self.edad}"
class Ave(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()
    def __str__(self):
        return f"Nombre:{self.name} - Raza {self.raza} - Edad{self.edad}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to='avatares', null=True, blank= True)
    def __str__(self):
        return f"User:{self.user} - Imagen:{self.imagen}"

class Post(models.Model):
    titulo=models.CharField(max_length=250)
    contenido=models.TextField()
    fecha=models.DateField()
    def __str__(self):
        return f"Titulo:{self.titulo} - Contenido:{self.contenido} - Fecha:{self.fecha}"