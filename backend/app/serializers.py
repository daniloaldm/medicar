from rest_framework import serializers
from .models import (Especialidade, Medico, Agenda)

class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Especialidade
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Medico
        fields = '__all__'
        depth = 1

class AgendaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Agenda
        fields = ['medico', 'dia', 'horarios']
        depth = 2