from django.db import models

# Create your models here.

class Newtask(models.Model):
    name = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)
    tarea = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    solot = models.IntegerField()
    idSGA = models.IntegerField()
    numServicio = models.IntegerField()
    fechaAtencion = models.DateField(auto_now_add=False)
    horaAtencion = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name

