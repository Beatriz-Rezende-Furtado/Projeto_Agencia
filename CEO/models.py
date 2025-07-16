from django.db import models

# Create your models here.

class CEO(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='CEO/', blank=True)

    def __str__(self):
        return self.nome
