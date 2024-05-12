from django import forms
from movieapp.models import movieapp

class Movieform(forms.ModelForm):
    class Meta:
        model=movieapp
        fields='__all__'