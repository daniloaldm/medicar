from __future__ import unicode_literals
from django.db import migrations, models
import datetime
from django.db.models.signals import post_save 
from django.core.validators import *
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField

class Especialidade(models.Model):
    POST_STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )

    especialidade = models.CharField(max_length=200)
    ordering = ['id']

    def __str__(self):
        return f"{self.especialidade}"


class Medico(models.Model):
    POST_STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )

    nome = models.CharField(max_length=100, unique=True)
    crm =  models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
    ordering = ['id']

    def __str__(self):
        return f"{self.nome} "

class Agenda(models.Model):

    POST_STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia =  models.DateField()
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['dia']
        unique_together = [['medico', 'dia']]

    def __str__(self):
        return f"{self.dia} {self.horarios}"
        # return "Medico: " + str(self.medico.nome) + ", Especialidade: " + str(self.medico.especialidade) + ", Dia: " + str(self.dia) + ", Horario: " + str(self.horarios) + ", Disponibilidade: " + str(self.disponivel)

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
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now=True)
    medico = models.ManyToManyField(Medico)

    def __str__(self):
        return f"{self.dia} {self.horario} {self.data_agendamento} {self.medico}"