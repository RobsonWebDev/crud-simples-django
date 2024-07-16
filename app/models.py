from django.db import models

class Pessoa(models.Model):

    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    show = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'