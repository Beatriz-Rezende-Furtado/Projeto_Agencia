from django.db import models

# Create your models here.
class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='modelos/', blank=True)

    def __str__(self):
        return self.nome
    
    