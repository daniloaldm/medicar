from rest_framework import serializers
from .models import (Especialidade, Medico, Agenda, Consulta, Horario, userProfile)
from datetime import date
from .validators import *


class getDefaultUser:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user

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
    medico = MedicoSerializer()
    horarios = serializers.StringRelatedField(many=True, source='horarios_disponiveis')

    class Meta:
        model = Agenda
         
        fields = (
            'id',
            'medico',
            'dia',
            'horarios'
        )

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

    paciente = serializers.HiddenField(default=getDefaultUser())

    class Meta:
        model = Consulta
        extra_kwargs = {
            'id_agenda': {'write_only': True},
            'paciente': {'write_only': True}
        }
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico', 'paciente', 'id_agenda']

    def validate(self, data):

        agenda = data['id_agenda']
        horario = data['horario']

        if Validators().verificar_se_data_Esta_Expirada(agenda.dia, horario):
            raise serializers.ValidationError("Data e Hora são menores que a data Atual")

        if Validators().verificar_se_usuario_esta_cadastrado_no_mesmo_dia(agenda.dia, horario, data['paciente']):
            raise serializers.ValidationError("Paciente já possuí data e horario marcados para esse horário")

        if Validators().agenda_ja_esta_alocada(agenda.pk, horario):
            raise serializers.ValidationError('Agenda em uso')

        if not agenda.horarios.filter(disponivel=True, horario=horario).exists():
            raise  serializers.ValidationError('Horário indisponível')

        return data

    def create(self, data):
        agenda = data.pop('id_agenda')

        return Consulta.objects.create(
            dia=agenda.dia,
            agenda=agenda,
            paciente=data['paciente'],
            horario=data['horario']
        )