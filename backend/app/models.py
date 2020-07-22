# -*- coding: utf-8 -*-
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

    nome = models.CharField(max_length=200)
    crm =  models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    unique_together = ['crm', 'telefone', 'email']
    ordering = ['id']

    def __str__(self):
        return self.nome

