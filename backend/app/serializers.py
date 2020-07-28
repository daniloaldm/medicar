from rest_framework import serializers
from .models import (Especialidade, Medico, Agenda, Consulta, Horario, userProfile)
import datetime

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
    paciente = userProfile()
    dia = serializers.StringRelatedField(read_only=True, source='agenda.dia')
    # horario = serializers.StringRelatedField(read_only=True, source='horario.horario')
    medico = MedicoSerializer(read_only=True, source='agenda.medico')
    
    # def validate(self, data):
    #     data_atual = datetime.date.today()
    #     now = datetime.datetime.now() 
    #     hora_atual = now.strftime("%m/%d/%Y, %H:%M:%S")
    #     agenda_selecionada = data['agenda']

    #     consulta_paciente = Consulta.objects.all().filter(paciente=data['paciente'])

    #     if agenda_selecionada.dia < data_atual:
    #         raise serializers.DjangoValidationError('Não foi possível marcar consulta: Dia passado!')
    #     if (agenda_selecionada.dia == data_atual) and (agenda_selecionada.horario < hora_atual):
    #         raise serializers.DjangoValidationError('Não foi possível marcar consulta: Horário passado!')
    #     if consulta_paciente.filter(agenda__dia=agenda_selecionada.dia, agenda__horario=agenda_selecionada.horario):
    #         raise serializers.DjangoValidationError('Não foi possível marcar consulta: Há uma outra consulta marcada para mesmo dia e horário!')
    
    #     return data

    class Meta:
        model = Consulta
        extra_kwargs = {
            'agenda': {'write_only': True},
            'paciente': {'write_only': True}
        }
        fields = '__all__'

