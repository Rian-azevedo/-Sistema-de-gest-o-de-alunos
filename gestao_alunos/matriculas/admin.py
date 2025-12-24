from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'status', 'data_matricula', 'nota_final')
    list_filter = ('status', 'curso')
    search_fields = ('aluno__nome', 'curso__nome')
    ordering = ('-data_matricula',)
    
    
    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request, obj, form, change)

# Register your models here.
