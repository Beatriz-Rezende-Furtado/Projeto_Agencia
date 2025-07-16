from django import forms
from .models import Estilista

class EstilistaForm(forms.ModelForm):
    class Meta:
        model = Estilista
        fields = ['nome', 'idade', 'bio', 'foto']