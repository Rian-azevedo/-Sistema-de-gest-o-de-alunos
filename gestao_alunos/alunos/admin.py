from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula')
    search_fields = ('nome', 'email')
    
# Register your models here.