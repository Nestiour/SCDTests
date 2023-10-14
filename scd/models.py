from django.db import models
from django.utils import timezone

# Create your models here.

class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True)
    anio = models.CharField(max_length=1, blank=False)
    division = models.CharField(max_length=1, blank=False)
    especialidad = models.CharField(max_length=15, blank=False)
    turno = models.CharField(max_length=8, blank=False)
 
    def __str__(self):
        return f"{self.id_cur} {self.anio} {self.division} {self.especialidad} {self.turno}"

class Docente(models.Model):
    id_doc = models.AutoField(primary_key=True)
    cuil = models.IntegerField(unique=True, blank=False)
    nombre = models.CharField(max_length=45, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    celular = models.CharField(max_length=15, blank=False)
    email = models.CharField(max_length=40, blank=False)
    domicilio = models.CharField(max_length=40, blank=False)
    localidad = models.CharField(max_length=30, blank=False)
    provincia = models.CharField(max_length=30, blank=False)
    genero = models.CharField(max_length=1, blank=False)
    estado = models.CharField(max_length=1, blank=False)
    #estado = models.BooleanField(default=True, blank=False)
    
    def __str__(self):
        return f"{self.id_doc} {self.cuil} {self.nombre} {self.apellido} {self.celular} {self.email}{self.domicilio}{self.localidad}{self.provincia} {self.genero} {self.estado}"

class Horario(models.Model):
    id_hor = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=1, blank=False)
    h_i = models.CharField(max_length=1, blank=False)
    h_f = models.CharField(max_length=1, blank=False)
    def __str__(self):
        return f"{self.id_hor} {self.dia} {self.h_i} {self.h_f}"
    
class Materia(models.Model):
    id_mat = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f"{self.id_mat} {self.nombre}"
    
class doc_mat(models.Model):
    id_dm = models.AutoField(primary_key=True)
    id_doc = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_mat = models.ForeignKey(Materia, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_dm} {self.id_doc} {self.id_mat}"
    
class Clase(models.Model):
    id_cla = models.AutoField(primary_key=True)
    id_hor = models.ForeignKey(Horario, on_delete=models.CASCADE)
    id_cur = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_dm = models.ForeignKey(doc_mat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_cla} {self.id_hor} {self.id_cur} {self.id_dm}"

class Asistencia(models.Model):
    id_asi = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now, blank=False)
    asistencia = models.CharField(max_length=1, blank=False)
    articulo = models.CharField(max_length=20, blank=True)
    id_cla = models.ForeignKey(Clase, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_asi} {self.asistencia} {self.articulo} {self.fecha}"