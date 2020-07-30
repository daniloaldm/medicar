 
from datetime import date, datetime
from rest_framework.filters import BaseFilterBackend
from django.db.models import Case, Q, Value, When

class AgendasFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        medico = request.query_params.getlist("medico")
        especialides = request.query_params.getlist("especialidade")
        data_inicio = request.query_params.get("data_inicio", None)
        data_fim = request.query_params.get("data_final", None)

        agendas = queryset.filter(
            medico__in=medico,
            medico__especialidade__id__in=especialides,
        )

        if data_inicio and data_fim:
            agendas = agendas.filter(dia__range=[data_inicio, data_fim])

        return agendas

class ConsultasFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        diaAtual = date.today()
        horaAtual = datetime.now().strftime('%H:%M')

        return queryset.filter(
            paciente=request.user,
            dia__gte=date.today(),
            horario__gte=Case(
                When(
                    Q(agenda__dia=diaAtual), then=Value(horaAtual)
                ),
                default=Value('00:00')
            )
        )