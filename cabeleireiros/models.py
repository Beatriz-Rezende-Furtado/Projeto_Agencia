
from django.db import models

class Cabeleireiro(models.Model):  
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='cabeleireiros/', blank=True)

    def __str__(self):
        return self.nome
    
    
