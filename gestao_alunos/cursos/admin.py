from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'carga_horaria', 'professor')
    search_fields = ('nome', 'codigo')
    

# Register your models here.