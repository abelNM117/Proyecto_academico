from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=75)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre    



class rol_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    estado= models.BooleanField(default=True)


# Create your models here.
