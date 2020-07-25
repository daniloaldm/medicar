from rest_framework import serializers
from .models import (Especialidade, Medico, Agenda, Consulta, Horarios, userProfile)

class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = '__all__'
        depth = 1

class HorariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horarios
        fields = ['horarios']

class AgendaSerializer(serializers.ModelSerializer):

    horarios = HorariosSerializer(many=True, read_only=True)
    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']
        depth = 2

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
        # depth = 2

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=userProfile
        fields='__all__'

