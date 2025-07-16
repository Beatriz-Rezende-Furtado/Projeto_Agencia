from django import forms
from .models import Fotografo

class FotografoForm(forms.ModelForm):
    class Meta:
        model = Fotografo
        fields = ['nome', 'idade', 'bio', 'foto']
        
        