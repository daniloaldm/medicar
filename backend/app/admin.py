from django.contrib import admin
from .models import (Especialidade, Medico, Agenda, Horario)

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

class HorarioInlineAdmin(admin.StackedInline):
    model = Horario
    extra = 1


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'medico', 'dia')
    inlines = [HorarioInlineAdmin,]

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)