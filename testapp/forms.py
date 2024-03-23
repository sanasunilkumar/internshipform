from django import forms
from testapp.models import Empmodel
class Empform(forms.ModelForm):
    class Meta:
        model=Empmodel
        fields='__all__'

