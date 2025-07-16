from django.db import models

# Create your models here.
from django.db import models

class Profissional(models.Model):
    CATEGORIAS = [
        ('modelo',     'Modelo'),
        ('fotografo',  'Fotógrafo'),
        ('produtor',   'Produtor'),
        ('maquiador',  'Maquiador'),
        ('estilista',  'Estilista'),
        ('cabeleleiro','Cabeleleiro'),
    ]

    nome      = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    bio       = models.TextField(blank=True)
    foto      = models.ImageField(upload_to='profissionais/', blank=True)

    def __str__(self):
        return self.nome