from django.db import models
from alunos.models import Aluno
from cursos.models import Curso
from django.core.exceptions import ValidationError

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
        constraints = [
            models.UniqueConstraint(
                fields=['aluno','curso'],
                name='unique_aluno_curso'
            )
        ]
        
    def __str__(self):
        return f"{self.aluno} - {self.curso}"

    def clean(self):
        if Matricula.objects.filter(
            aluno=self.aluno,
            curso=self.curso
        ).exclude(pk=self.pk).exists():
            raise ValidationError(
                'Este aluno já está matriculado neste curso'
            )
# Create your models here.