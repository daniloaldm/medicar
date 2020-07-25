from django.contrib import admin
from .models import (Especialidade, Medico, Agenda, Horarios)

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

class HorariosInlineAdmin(admin.StackedInline):
    model = Horarios
    extra = 1


class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'medico',
        'dia',
        'horarios',
        'disponivel'
    ]
    
    inlines = [HorariosInlineAdmin,]

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)