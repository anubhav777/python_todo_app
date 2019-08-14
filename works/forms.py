from .models import Todowoorks
from django import forms


class Todo_Forms(forms.ModelForm):
    class Meta:
        model=Todowoorks
        fields=['workname','status','fileupload']