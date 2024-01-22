from django.db import models
# from ESTUDIANTE.models import matricula, curso_paralelo, trimestre_parcial, genero, etnia, tipo_sangre, tipo_documento, jornada, periodo
from ESTUDIANTE.models import *
from django.contrib.auth.models import User

class materia(models.Model):
    nombre_materia= models.CharField(max_length=25)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_materia
    
class profesor(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre= models.CharField(max_length=45)
    apellido= models.CharField(max_length=45)
    estado_civil= models.CharField(max_length=20)
    tipo_documento= models.ForeignKey(tipo_documento, on_delete=models.CASCADE)
    N_documento= models.CharField(max_length=15)
    genero= models.ForeignKey(genero, on_delete=models.CASCADE)
    nacionalidad= models.CharField(max_length=20)
    nacimiento_fecha= models.DateField()
    etnia= models.ForeignKey(etnia, on_delete=models.CASCADE)
    direccion= models.CharField(max_length=50)
    correo= models.CharField(max_length=50)
    telefono= models.CharField(max_length=12)
    especialidad=models.CharField(max_length=200)
    tipo_sangre = models.ForeignKey(tipo_sangre, on_delete=models.CASCADE)
    tiene_discapacidad= models.CharField(max_length=10)
    tipo_discapacidad= models.CharField(max_length=50)
    carnet_discapacidad=models.CharField(max_length=15)
    estado= models.BooleanField(default=True)
    imagen= models.ImageField(upload_to="PROFESORES", null=True)
    def __str__ (self):
        return self.nombre +" "+ self.apellido
    


class profesor_cur_materia(models.Model):
    curso_paralelo= models.ForeignKey(curso_paralelo,on_delete=models.CASCADE)
    materia= models.ForeignKey(materia,on_delete=models.CASCADE)
    profesor=models.ForeignKey(profesor,on_delete=models.CASCADE)
    jornada= models.ForeignKey(jornada,on_delete=models.CASCADE)
    periodo= models.ForeignKey(periodo,on_delete=models.CASCADE)
    estado= models.BooleanField(default=True)


class notas(models.Model):
    matricula= models.ForeignKey(matricula,on_delete=models.CASCADE)
    jornada= models.ForeignKey(jornada,on_delete=models.CASCADE)
    materia= models.ForeignKey(materia, on_delete=models.CASCADE)
    puntaje1 = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    puntaje2 = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    puntaje3 = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    promedio_general=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    registro= models.CharField(max_length=100)
    estado= models.BooleanField(default=True)


