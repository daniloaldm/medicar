from django.urls import path, include
from rest_framework import routers
from .views import (EspecialidadeView, MedicoView, AgendaView)

router = routers.DefaultRouter()
router.register(r'medicos', MedicoView)
router.register(r'especialidades', EspecialidadeView)
router.register(r'consultas', AgendaView)

urlpatterns = [
    path('', include(router.urls)),
]