from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import (Especialidade, Medico)
from .serializers import (EspecialidadeSerializer, MedicoSerializer)

class EspecialidadeView(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_fields = ['especialidade']

class MedicoView(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_fields = ['nome', 'especialidade']