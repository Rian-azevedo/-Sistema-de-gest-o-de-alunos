from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.full_clean
        super().save_model(request, obj, form, change)

# Register your models here.
