from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome