from django.db import models
from professores.models import Professor

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    carga_horaria = models.PositiveIntegerField()
    Professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    
    def __str__(Self):
        return f"{self.nome} ({self.codigo})"
    
# Create your models here.

