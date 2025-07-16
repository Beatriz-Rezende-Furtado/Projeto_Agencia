from django import forms
from .models import CEO

class CEOForm(forms.ModelForm):
    class Meta:
        model = CEO
        fields = ['nome', 'bio', 'foto']