from django.contrib import admin
from .models import (Especialidade, Medico, Agenda)

# Register your models here.
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'crm',
        'email',
        'telefone',
        'especialidade'
    ]

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = [
        'especialidade'
    ]

class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'medico',
        'dia',
        'horarios',
        'disponivel'
    ]

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)