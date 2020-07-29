from rest_framework import serializers
from .models import (Especialidade, Medico, Agenda, Consulta, Horario, userProfile)
from datetime import date

class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(many=False, read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']

class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = ['horario']

class AgendaSerializer(serializers.ModelSerializer):

    horario = HorarioSerializer(many=True, read_only=True)
    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horario']
        depth = 2

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=userProfile
        fields='__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    id_agenda = serializers.PrimaryKeyRelatedField(
        queryset=Agenda.objects.filter(dia__gte=date.today()),
        write_only=True,
        label='agenda'
    )

    dia = serializers.DateField(source="agenda.dia", read_only=True)
    
    medico = MedicoSerializer(source="agenda.medico", read_only=True)

    paciente = userProfile()

    class Meta:
        model = Consulta
        extra_kwargs = {
            'id_agenda': {'write_only': True},
            'paciente': {'write_only': True}
        }
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico', 'paciente', 'id_agenda']

    def create(self, data):
        agenda = data.pop('id_agenda')

        return Consulta.objects.create(
            dia=agenda.dia,
            agenda=agenda,
            paciente=data['paciente'],
            horario=data['horario']
        )