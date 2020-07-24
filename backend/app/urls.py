from django.urls import path, include
from rest_framework import routers
from .views import (EspecialidadeView, MedicoView, AgendaView, ConsultaView)

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeView)
router.register(r'medicos', MedicoView)
router.register(r'agendas', AgendaView)
router.register(r'consultas', ConsultaView)

urlpatterns = [
    path('', include(router.urls)),
]