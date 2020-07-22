from django.contrib import admin
from .models import (Especialidade, Medico)

# Register your models here.
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'crm',
        'email',
        'telefone'
    ]

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = [
        'especialidade'
    ]

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)