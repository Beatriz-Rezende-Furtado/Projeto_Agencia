from django.db import models

# Create your models here.
from django.db import models

class Maquiador(models.Model):  # nome da classe no singular
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='maquiadores/', blank=True)

    def __str__(self):
        return self.nome