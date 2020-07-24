from __future__ import unicode_literals
from django.db import migrations, models
from django.utils import timezone
from django.core.validators import *
from django.contrib.auth.models import User

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

    dia =  models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(default=timezone.now(), editable=False)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    class Meta:
        ordering = ['dia']
        unique_together = ['dia', 'horario', 'medico']

    def __str__(self):
        return f"{self.dia} {self.horario} {self.data_agendamento} {self.medico}"
        