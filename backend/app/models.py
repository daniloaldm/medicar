from django.db import migrations, models
import datetime
from django.core.validators import *
from django.contrib.auth.models import User
from .managers import *
from .validators import *
from django.core.exceptions import ValidationError


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

    def validar_data_de_agendamento(value):
        diaDeHoje = date.today()
        if (value < diaDeHoje):
            raise ValidationError('A Data Não pode Ser Menor Que a Data Atual')

    medico = models.ForeignKey(Medico, related_name='medico', on_delete=models.CASCADE)
    dia = models.DateField(validators=[validar_data_de_agendamento])
    objects = models.Manager()
    disponivel = AgendaDisponivelManager.from_queryset(AgendaQuerySet)()

    class Meta:
        unique_together = ['medico', 'dia']
        ordering = ['dia']

    def __str__(self):
        return self.dia.strftime("%d/%m/%Y")

class Horario(models.Model):

    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.PROTECT)
    horario = models.TimeField()
    disponivel = models.BooleanField('disponível', default=True, editable=False)

    class Meta:
        unique_together = ['agenda', 'horario']
        ordering = ['horario']

    def __str__(self):
        return self.horario.strftime('%H:%M')

class Consulta(models.Model):
    dia = models.DateField()
    agenda = models.ForeignKey(Agenda, related_name="agenda", on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now=True, editable=False)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['dia', 'horario']

    def __str__(self):
        return self.data_agendamento.strftime("%H:%M")
    
    
class userProfile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    def __str__(self):
        return self.user.username