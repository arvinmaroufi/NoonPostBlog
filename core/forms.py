from django import forms
from .models import Newsleter



class NewsleterForm(forms.ModelForm):
    class Meta:
        model=Newsleter
        fields=['email']