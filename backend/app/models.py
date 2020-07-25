from django.db import migrations, models
import datetime
from django.core.validators import *
from django.contrib.auth.models import User

class Especialidade(models.Model):

    especialidade = models.CharField(max_length=200)
    ordering = ['id']

    def __str__(self):
        return f"{self.especialidade}"


class Medico(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    crm =  models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} "

class Agenda(models.Model):

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia =  models.DateField()
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        unique_together = [['medico', 'dia']]

    def __str__(self):
        return f"{self.dia} {self.horarios}"
 
    @property
    def horarios(self):
        return list(self.horarios_set.all())

class Horarios(models.Model):
    horarios = models.TimeField(blank=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    class Meta:
        ordering = ['horarios']
        unique_together = [['horarios', 'agenda']] 

    def __str__(self):
        return f"{self.horarios}"

class Consulta(models.Model):
    dia =  models.DateField()
    horario = models.TimeField(blank=False)
    data_agendamento = models.DateTimeField(auto_now=True)
    medico = models.ManyToManyField(Medico)

    def __str__(self):
        return f"{self.dia} {self.horario} {self.data_agendamento} {self.medico}"

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_organizer=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username