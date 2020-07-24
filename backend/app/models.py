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
    horarios = models.TimeField()
    disponivel = models.BooleanField(default=True)
    
    def clean(self):
        data_atual = datetime.date.today()
        hora_atual = datetime.datetime.now().time()
        
        if self.dia < data_atual:
            raise serializers.DjangoValidationError('Não é permitido criar agenda para dia passado!')
        if (self.dia == data_atual) and (self.horarios < hora_atual):
            raise serializers.DjangoValidationError('Não é permitido criar agenda para horario passado!')

    # data_agendamento = models.DateTimeField(default=timezone.now(), editable=False)


    class Meta:
        ordering = ['dia']
        unique_together = [['medico', 'dia', 'horarios']]

    def __str__(self):
        return f"{self.dia} {self.horarios}"
        # return "Medico: " + str(self.medico.nome) + ", Especialidade: " + str(self.medico.especialidade) + ", Dia: " + str(self.dia) + ", Horario: " + str(self.horarios) + ", Disponibilidade: " + str(self.disponivel)
        
class Consulta(models.Model):
    dia =  models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True)
    medico = models.ManyToManyField(Medico)

    def __str__(self):
        return f"{self.dia} {self.horario} {self.data_agendamento} {self.medico}"