from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tipo_documento(models.Model):
    name_td = models.CharField(max_length=75)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.name_td
    

class genero(models.Model):
    name_g = models.CharField(max_length=20)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.name_g
    
class tipo_sangre(models.Model):
    name_ts = models.CharField(max_length=15)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.name_ts
    
class etnia(models.Model):
    name_et = models.CharField(max_length=15)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.name_et

class jornada(models.Model):
    nombre_jornada= models.CharField(max_length=50)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_jornada
    
class periodo(models.Model):
    nombre_periodo= models.CharField(max_length=50)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_periodo

class curso(models.Model):
    nombre_curso= models.CharField(max_length=50, null=True)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_curso
    
class paralelo(models.Model):
    nombre_paralelo= models.CharField(max_length=50)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_paralelo


class trimestre(models.Model):
    nombre_trimestre= models.CharField(max_length=50)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_trimestre

class parcial(models.Model):
    nombre_parcial= models.CharField(max_length=25)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_parcial

class trimestre_parcial(models.Model):
    trimestre = models.ForeignKey(trimestre,on_delete=models.CASCADE)
    parcial= models.ForeignKey(parcial,on_delete=models.CASCADE)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return f"{self.trimestre.nombre_trimestre} {self.parcial.nombre_parcial}" 

class curso_paralelo(models.Model):
    curso = models.ForeignKey(curso,on_delete=models.CASCADE)
    paralelo= models.ForeignKey(paralelo,on_delete=models.CASCADE)
    estado= models.BooleanField(default=True) 
    def __str__(self):
        return f"{self.curso.nombre_curso} {self.paralelo.nombre_paralelo}"  

    

    
class estudiantes(models.Model):
    
    nombre= models.CharField(max_length=45)
    apellido= models.CharField(max_length=45)
    documento = models.CharField(max_length=10)
    nacimiento_fecha= models.DateField()
    correo= models.EmailField()
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    nacionalidad = models.CharField(max_length=30)
    dtest_edad =  models.CharField(max_length=30)
    repre_cedula = models.CharField(max_length=10)
    repre_nomape = models.CharField(max_length=70)
    repre_celular = models.CharField(max_length=10)
    repre_convencional = models.CharField(max_length=10)
    repre_gmail = models.EmailField(max_length=100)
    madre_cedula = models.CharField(max_length=10)
    madre_nomape =  models.CharField(max_length=70)
    infmadre_celular = models.CharField(max_length=10)
    infmadre_convencional = models.CharField(max_length=10)
    infmadre_gmail = models.EmailField(max_length=100)
    infpadre_cedula = models.CharField(max_length=10)
    infpadre_nomap = models.CharField(max_length=70)
    infpadre_celular =  models.CharField(max_length=10)
    infpadre_convencional =  models.CharField(max_length=10)
    infpadre_gmail = models.EmailField(max_length=100)
    estsalud_alergias =models.CharField(max_length=10) 
    estsalud_tipoalerg = models.CharField(max_length=50)
    estsalud_vacuna19 = models.CharField(max_length=10)
    tiene_discapacidad = models.CharField(max_length=10)
    estsalud_discapatipo = models.CharField(max_length=10)
    estemergencia_numerocell1 = models.CharField(max_length=10)
    estemergencia_nombre1 =  models.CharField(max_length=10)
    estemergencia_numcell2 = models.CharField(max_length=10)
    estemergencia_nombre2 = models.CharField(max_length=10)
    genero= models.ForeignKey(genero, on_delete=models.CASCADE)
    tipo_documento= models.ForeignKey(tipo_documento,on_delete=models.CASCADE)
    tipo_sangre =models.ForeignKey(tipo_sangre,on_delete=models.CASCADE)
    etnia = models.ForeignKey(etnia,on_delete=models.CASCADE)
    usuariox=models.ForeignKey(User, on_delete=models.CASCADE)
    estado= models.BooleanField(default=True)
    imagen= models.ImageField(upload_to="ESTUDIANTE", null=True)
    


class matricula(models.Model):
    estudiante =models.ForeignKey(estudiantes,on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo,on_delete=models.CASCADE)
    jornada=models.ForeignKey(jornada, on_delete=models.CASCADE)
    curso_paralelo=models.ForeignKey(curso_paralelo,on_delete=models.CASCADE)
    estado= models.BooleanField(default=False)
    def __str__(self):
        return self.estudiante 