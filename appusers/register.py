from django import forms
from .models import Allusers

class Userregister(forms.ModelForm):
    class Meta:
        model=Allusers
        fields=['fullname','email','address','password']
