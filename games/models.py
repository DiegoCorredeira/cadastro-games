from django.db import models

# Create your models here.


class Games(models.Model):
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    qtd_trofeus = models.IntegerField()

    def __str__(self) -> str:
        return self.game()