from django.urls import path, include
from rest_framework import routers
from .views import (EspecialidadeView, MedicoView, AgendaView, ConsultaView,  UserProfileListCreateView, userProfileDetailView)

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeView)
router.register(r'medicos', MedicoView)
router.register(r'agendas', AgendaView)
router.register(r'consultas', ConsultaView)

urlpatterns = [
    path('', include(router.urls)),
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]