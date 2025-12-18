from django.db import models
from alunos.models import Aluno
from cursos.models import Curso

class Matricula(models.Model):
    aluno = models.ForeignKey(
        'alunos.Aluno',
        on_delete=models.CASCADE,
        related_name='matriculas'
        )
    
    curso = models.ForeignKey(
        'cursos.Curso',
        on_delete=models.CASCADE,
        related_name='matriculas'
        )
    
    data_matricula = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('ATIVO', 'ativo'),
        ('TRANCADO', 'trancado'),
        ('CONCLUIDO', 'concluido'),
    ], default='ATIVO'
                              )
    
    nota_final = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank =True
    )
    
    class Meta:
        unique_together = ('aluno', 'curso')
        
    def __init__(self):
        return f"{self.aluno} - {self.curso}"

# Create your models here.