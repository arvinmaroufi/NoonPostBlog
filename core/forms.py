from django import forms
from .models import Newsleter,ContactUs



class NewsleterForm(forms.ModelForm):
    class Meta:
        model=Newsleter
        fields=['email']
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        

