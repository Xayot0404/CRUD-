from .models import CRUDmodel
from django import forms

class CRUDform(forms.ModelForm):
    class Meta:
        model = CRUDmodel
        fields = '__all__'