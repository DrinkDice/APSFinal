from django.db import models

class Filmes(models.Model):
    nome_filme = models.CharField(max_length=255, default='')
    data_lancamento = models.DateField(default='')
    nome_diretor = models.CharField(max_length=255, default='')
    nota = models.DecimalField(max_digits=3, decimal_places=1, default='0')

    def __str__(self):
        return f'Nome: {self.nome_filme} | Nota: {self.nota}'

