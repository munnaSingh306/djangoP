from django import forms
from CRUDoperations.models import customer


class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
