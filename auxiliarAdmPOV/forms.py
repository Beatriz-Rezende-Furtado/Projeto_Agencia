from django.forms import ModelForm
from .models import Profissional

class ProfissionalForm(ModelForm):
    class Meta:
        model  = Profissional
        fields = ['nome', 'categoria', 'bio', 'foto']
