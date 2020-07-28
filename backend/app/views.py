from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.filters import SearchFilter
from .permissions import IsOwnerProfileOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from .models import (Especialidade, Medico, Agenda, Consulta, Horario, userProfile)
from .serializers import (EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer, HorarioSerializer, userProfileSerializer)

class EspecialidadeView(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    # permission_classes=[IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['especialidade']

class MedicoView(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    # permission_classes=[IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nome']

class AgendaView(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    # permission_classes=[IsAuthenticated]
    filter_fields = ['medico', 'dia', 'disponivel']

class ConsultaView(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    # permission_classes=[IsAuthenticated]
    filter_fields = '__all__'

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    # permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]