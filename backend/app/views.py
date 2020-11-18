from rest_framework import viewsets, filters, generics
from rest_framework.filters import SearchFilter
from .permissions import IsOwnerProfileOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from .models import (Especialidade, Medico, Agenda, Consulta, Horario, userProfile)
from .serializers import (EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer, HorarioSerializer, userProfileSerializer)
from .filtersCustom import *
from rest_framework import mixins

class EspecialidadeView(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    # permission_classes=[IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['especialidade']

class MedicoView(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    # permission_classes=[IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nome']

class AgendaView(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Agenda.disponivel.prefetch_horarios_disponiveis()
    serializer_class = AgendaSerializer
    # permission_classes=[IsAuthenticated]
    ordering_fields = ['dia']
    filter_fields = '__all__'

class ConsultaView( mixins.ListModelMixin, 
        mixins.CreateModelMixin, 
        mixins.DestroyModelMixin, 
        viewsets.GenericViewSet
        ):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    # permission_classes=[IsAuthenticated]
    filter_fields = '__all__'

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]