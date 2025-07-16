from django import forms
from .models import Produtor

class ProdutorForm(forms.ModelForm):
    class Meta:
        model = Produtor
        fields = ['nome', 'idade', 'bio', 'foto']
        
        