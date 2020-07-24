from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import (Especialidade, Medico, Agenda, Consulta)
from .serializers import (EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer)

class EspecialidadeView(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_fields = ['especialidade']

class MedicoView(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_fields = ['nome', 'especialidade']

class AgendaView(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_fields = ['disponivel', 'medico', 'dia', 'horarios']

class ConsultaView(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_fields = '__all__'