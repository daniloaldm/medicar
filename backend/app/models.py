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
    dia = models.DateField()
    horario = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def clean(self):
        data_atual = datetime.date.today()
        
        if self.dia < data_atual:
            raise serializers.DjangoValidationError('Não é permitido criar agenda para dia passado!')
        if (self.dia == data_atual) and (self.horario < hora_atual):
            raise serializers.DjangoValidationError('Não é permitido criar agenda para horario passado!')
        
    class Meta:
        unique_together = ['medico', 'dia']

    def __str__(self):
        return f"{self.medico} {self.dia} {self.horario}"
 
    @property
    def horario(self):
        return list(self.horario_set.all())

class Horario(models.Model):
    horario = models.TimeField(blank=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    class Meta:
        ordering = ['horario']
        unique_together = ['horario', 'agenda']

    def __str__(self):
        return f"{self.horario}"

class Consulta(models.Model):
    agenda = models.OneToOneField(Agenda, on_delete=models.CASCADE)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now=True)
    
class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    def __str__(self):
        return self.user.username