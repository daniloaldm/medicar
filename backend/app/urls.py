from django.urls import path, include
from rest_framework import routers
from .views import (EspecialidadeView, MedicoView)

router = routers.DefaultRouter()
router.register(r'medicos', MedicoView)
router.register(r'especialidades', EspecialidadeView)

urlpatterns = [
    path('', include(router.urls)),
]