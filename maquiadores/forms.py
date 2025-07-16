from django import forms
from .models import Maquiador

class MaquiadorForm(forms.ModelForm):
    class Meta:
        model = Maquiador
        fields = ['nome', 'idade', 'bio', 'foto']
        