from datetime import datetime

from .models import *


class Validators:

    def verificar_se_data_Esta_Expirada(self, dia, hora):

        verificar_data = datetime.strptime(
            f'{dia} {hora}', "%Y-%m-%d %H:%M:%S")

        return verificar_data < datetime.today()

    def verificar_se_usuario_esta_cadastrado_no_mesmo_dia(self, dia, hora, paciente):
        from .models import Consulta
        Consulta.objects.filter(
            dia=dia,
            horario=hora,
            paciente=paciente
        ).exists()

    def agenda_ja_esta_alocada(self, agenda, hora):
        from .models import Consulta
        Consulta.objects.filter(
            agenda__id=agenda,
            horario=hora
        ).exists()