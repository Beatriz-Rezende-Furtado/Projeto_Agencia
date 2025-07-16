from django import forms
from .models import Cabeleireiro

class CabeleireiroForm(forms.ModelForm):
    class Meta:
        model = Cabeleireiro
        fields = ['nome', 'idade', 'bio', 'foto']
        
        
        