from tkinter import Widget
from .models import Entries
from django import forms

class Entries_form(forms.ModelForm):
    class Meta:
        model=Entries
        fields=['name','price','type','description']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'})
        }